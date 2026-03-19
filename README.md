Brain Tumor Detection using Deep Learning (MobileNetV2)  
This project performs Brain Tumor Classification on MRI images using Deep Learning.  
The model predicts whether the MRI scan contains Glioma, Meningioma, Pituitary tumor, or No Tumor.

📌 Features  
Image preprocessing and normalization  
Data augmentation for better generalization  
Transfer Learning using MobileNetV2  
Classification into 4 tumor types  
Streamlit app for real-time prediction  

🛠️ Technologies Used  
Python  
TensorFlow / Keras (Deep Learning)  
NumPy (Numerical Operations)  
Streamlit (Web App Framework)  
PIL (Image Processing)  

⚙️ Project Workflow  

Image Preprocessing  
Resize images to 224x224 RGB  
Normalize pixel values  
Apply data augmentation  

Feature Extraction  
Use MobileNetV2 as pre-trained model  

Model Training  
Add custom layers (Dense, Dropout)  
Train on MRI dataset  
Fine-tune last layers  

Evaluation  
Predict tumor type  
Calculate accuracy and confidence  

Prediction  
Upload MRI image  
Model predicts tumor type with confidence score  

📊 Example  

Input:  
MRI Brain Image  

Output:  
Prediction: Glioma  
Confidence: 92.45%  

📂 Project Structure  
brain-tumor-detection  
│  
├── app.py  
├── brain_tumor_model.h5  
├── README.md  

🚀 Future Improvements  
Add Grad-CAM visualization  
Deploy on cloud  
Improve accuracy with larger dataset  

👨‍💻 Author  
Tanuj Kumar  
B.Tech CSE (AI & ML)  
Skills: Python | Machine Learning | Deep Learning | Computer Vision  
🔗 GitHub: https://github.com/tanujkumarpandranki/Brain_Tumor_DL_Project
