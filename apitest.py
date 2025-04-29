from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
from transformers import ViTForImageClassification, ViTImageProcessor
import io
import logging

app = FastAPI()

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once at startup (not in endpoint)
MODEL_PATH = "C:/Users/hrish/.cache/huggingface/hub/deepfake_vs_real_image_detection/snapshots/29e4cf9efc543845610045f6ba7e88e5cf9d9301"
model = ViTForImageClassification.from_pretrained(MODEL_PATH)
processor = ViTImageProcessor.from_pretrained(MODEL_PATH)

@app.get("/")
async def root():
    return {
        "message": "ViT Image Classification API",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "predict": "/predict (POST)"
        }
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # 1. Read the uploaded file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        
        # 2. Process image
        inputs = processor(images=image, return_tensors="pt")
        
        # 3. Run inference
        with torch.no_grad():
            outputs = model(**inputs)
        
        # 4. Get prediction
        predicted_label = outputs.logits.argmax(-1).item()
        class_name = model.config.id2label[predicted_label]
        confidence = torch.nn.functional.softmax(outputs.logits, dim=-1)[0][predicted_label].item()
        
        return {
            "predicted_class": class_name,
            "confidence": float(confidence),
            "class_id": predicted_label,
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))