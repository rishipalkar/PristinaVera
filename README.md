

## Deepfake Detector App – Project Explanation

This project is a mobile-based **deepfake detection system** that allows users to upload images or frames from videos and determine whether they are real or artificially generated (deepfakes). The system is composed of three main components: a **Flutter app for the user interface**, a **FastAPI backend** to handle API requests and communicate with the model, and a **Vision Transformer (ViT)** model trained to classify images as real or fake.

---

### 🔹 Objective

The primary goal is to build an easy-to-use mobile app that can detect deepfakes by analyzing images. Deepfakes are increasingly being used to spread misinformation, so tools like this can help verify media authenticity in real-time.

---

### 📱 Frontend: Flutter App

The mobile app, built using Flutter, provides a clean and intuitive interface where users can:

- Select an image from their gallery or take a new photo using the camera.
- Upload the image to the backend server for analysis.
- Receive a prediction indicating whether the image is “Real” or “Fake”.
- Optionally view the confidence score of the prediction.

The app uses common packages for image selection and sending HTTP requests. It’s designed to work smoothly across Android and iOS.

---

### 🌐 Backend: FastAPI Server

The FastAPI server acts as the communication bridge between the app and the deepfake detection model. It has the following roles:

- Receives image files sent by the Flutter app.
- Preprocesses the image to match the input format expected by the model.
- Passes the image to the Vision Transformer model for prediction.
- Sends back the results to the app in the form of a readable label (Real/Fake) and a confidence score.

It also includes cross-origin support so that mobile apps running on different platforms can access the API securely.

---

### 🧠 Model: Vision Transformer (ViT)

At the core of the detection system is the Vision Transformer model. This model is known for its strong performance in image classification tasks and is well-suited for spotting subtle manipulations typical in deepfakes.

The model is fine-tuned on publicly available deepfake datasets such as:

- FaceForensics++
- Celeb-DF
- DeepFake Detection Challenge (DFDC)

After training, the model is capable of analyzing an image and predicting whether it's real or fake with high accuracy.

---

### 🔄 Workflow

The overall workflow looks like this:

1. The user opens the app and selects or captures an image.
2. The image is uploaded to the FastAPI server.
3. The server processes the image and sends it to the Vision Transformer model.
4. The model returns a prediction.
5. The app displays the result to the user.

---

### 🚀 Key Features

- **Cross-platform compatibility**: Runs on both Android and iOS.
- **Real-time predictions**: Get results in seconds after uploading.
- **Confidence scores**: Users see not just the label, but how confident the model is.
- **Expandable design**: Can be extended to support videos, frame-by-frame analysis, or face regions only.
- **Secure backend**: API can be secured with authentication or rate limiting.
- **Modular architecture**: Each part of the system can be updated independently.

---

### 🌟 Possible Enhancements

- **Support for full video deepfake detection** by analyzing multiple frames.
- **Heatmap/attention visualization** to show users which parts of the image influenced the decision.
- **Cloud deployment** to scale the backend for multiple users.
- **Authentication features** to secure user data and prevent abuse.

---

This project brings together cutting-edge AI with accessible mobile technology to offer a practical tool for deepfake detection. It’s a strong showcase of how modern tools like Flutter, FastAPI, and transformers can be combined for impactful real-world applications.

---
