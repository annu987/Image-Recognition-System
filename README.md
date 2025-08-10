
# Image Recognition System

## Description  
Develop an image classification model to identify objects in images. Users can upload images through a web app and receive real-time predictions with confidence scores.

## Technologies  
- **Python:** TensorFlow/Keras, OpenCV, Pillow  
- **Backend:** Flask  
- **Frontend:** HTML, CSS (Bootstrap), JavaScript  
- **Model:** Pretrained MobileNetV2 on ImageNet for classification  

## Features  
- Upload images through a modern web interface  
- Real-time object classification with top 3 predictions  
- Displays uploaded image alongside predictions and probabilities  
- User-friendly responsive UI with Bootstrap  
- Modular code with clear separation of backend and frontend  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Image-Recognition-System.git
   cd Image-Recognition-System
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Upload an image and view the classification results.

## Project Structure

```
Image-Recognition-System/
├── app.py               # Flask backend application
├── model.py             # Model loading and prediction logic
├── templates/           # HTML templates (index.html, result.html)
├── static/
│   ├── uploads/         # Uploaded images
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
<img width="1440" height="900" alt="Screenshot 2025-08-10 at 4 46 32 PM" src="https://github.com/user-attachments/assets/1e65ec0a-099d-480f-8f0c-1d125f1b1eaa" />
<img width="1440" height="900" alt="Screenshot 2025-08-10 at 4 46 43 PM" src="https://github.com/user-attachments/assets/a0401839-3c81-4b06-9793-71fb9e8de1b2" />


## Future Enhancements

- Fine-tune the model on custom datasets for improved accuracy  
- Add batch image upload and prediction  
- Generate downloadable prediction reports (PDF/HTML)  
- Deploy on cloud platforms (Heroku, AWS, etc.) for wider accessibility  

## License

This project is licensed under the MIT License.

## Contact

**Mohammed Anaan**  
Email: zeb.begum786@gmail.com  


---

*This README describes an image recognition system built for internships and portfolio showcasing.*
