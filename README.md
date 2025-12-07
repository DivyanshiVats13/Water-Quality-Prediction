# 💧 Water Quality Prediction System

An AI-powered web application that predicts water safety using machine learning. This project analyzes 20 different water quality parameters to determine if water is safe for drinking.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Information](#dataset-information)
- [Model Details](#model-details)
- [UI/UX Design](#uiux-design)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

This project provides a **real-time water quality prediction system** that uses machine learning to classify water samples as safe or unsafe for consumption. The system analyzes chemical and biological parameters to make accurate predictions, helping ensure water safety.

### Key Highlights
- ✅ **20 Parameter Analysis** - Comprehensive water quality assessment
- ✅ **XGBoost ML Model** - High-accuracy gradient boosting classifier
- ✅ **Modern Web Interface** - Beautiful, animated, and user-friendly UI
- ✅ **Real-time Predictions** - Instant results with visual feedback
- ✅ **Responsive Design** - Works seamlessly on all devices

---

## ✨ Features

### Machine Learning
- **XGBoost Classifier** for robust predictions
- **StandardScaler** for feature normalization
- Pre-trained model with high accuracy
- Handles 20 different water quality parameters

### Web Application
- **Flask Backend** - Lightweight and efficient
- **Modern UI** - Gradient backgrounds, smooth animations
- **Interactive Forms** - 20 input fields with validation
- **Visual Feedback** - Color-coded results (safe/unsafe)
- **Responsive Design** - Mobile and desktop friendly

### User Experience
- Animated wave backgrounds
- Smooth transitions and hover effects
- Pulse animations on icons
- Bounce effects on results
- Professional typography (Inter font family)

---

## 📁 Project Structure

```
project int/
├── app.py                      # Flask application (main backend)
├── file1.ipynb                 # Jupyter notebook (model training & EDA)
├── waterQuality1.csv           # Dataset (7,999 samples)
├── water_xgb_model.pkl         # Trained XGBoost model
├── scaler.pkl                  # StandardScaler for preprocessing
├── templates/
│   └── index.html              # Frontend HTML with modern design
├── static/
│   └── styles.css              # CSS with animations and gradients
└── README.md                   # Project documentation
```

---

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **XGBoost** - Machine learning model
- **scikit-learn** - Data preprocessing and metrics
- **pandas** - Data manipulation
- **NumPy** - Numerical computations
- **pickle** - Model serialization

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **Font Awesome 6.4.0** - Icon library
- **Google Fonts (Inter)** - Typography

### Machine Learning
- **XGBoost Classifier** - Gradient boosting algorithm
- **StandardScaler** - Feature scaling
- **Train-Test Split** - Model validation

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd "project int"
```

### Step 2: Install Dependencies
```bash
pip install flask numpy pandas scikit-learn xgboost
```

### Step 3: Verify Files
Ensure the following files exist:
- `water_xgb_model.pkl` (trained model)
- `scaler.pkl` (feature scaler)
- `waterQuality1.csv` (dataset)

### Step 4: Run the Application
```bash
python3 app.py
```

The application will start on `http://127.0.0.1:5000`

---

## 💻 Usage

### Running the Web Application

1. **Start the server:**
   ```bash
   python3 app.py
   ```

2. **Open your browser:**
   Navigate to `http://127.0.0.1:5000`

3. **Enter water parameters:**
   Fill in all 20 chemical and biological parameters:
   - Aluminium, Ammonia, Arsenic, Barium, Cadmium
   - Chloramine, Chromium, Copper, Fluoride, Bacteria
   - Viruses, Lead, Nitrates, Nitrites, Mercury
   - Perchlorate, Radium, Selenium, Silver, Uranium

4. **Get prediction:**
   Click "Analyze Water Quality" to receive instant results

5. **Interpret results:**
   - ✅ **Green Result** - "Safe to Drink 💧"
   - ❌ **Orange/Red Result** - "Not Safe ❌"

### Example Input Values
```
Aluminium: 1.65
Ammonia: 9.08
Arsenic: 0.04
Barium: 2.85
Cadmium: 0.007
... (and so on for all 20 parameters)
```

---

## 📊 Dataset Information

### Source
- **File:** `waterQuality1.csv`
- **Samples:** 7,999 water quality measurements
- **Features:** 20 chemical and biological parameters
- **Target:** `is_safe` (binary: 0 = unsafe, 1 = safe)

### Class Distribution
- **Unsafe (0):** 7,084 samples (~88.6%)
- **Safe (1):** 912 samples (~11.4%)
- **Note:** Dataset is imbalanced, favoring unsafe samples

### Data Preprocessing
1. **Handling Missing Values:** Converted errors to NaN and dropped
2. **Type Conversion:** Ensured all features are numeric
3. **Scaling:** Applied StandardScaler for normalization
4. **Cleaning:** Removed 3 corrupted records with `#NUM!` errors

### Feature Statistics
| Parameter | Mean | Std Dev | Min | Max |
|-----------|------|---------|-----|-----|
| Aluminium | 0.67 | 1.27 | 0.00 | 5.05 |
| Arsenic | 0.16 | 0.25 | 0.00 | 1.05 |
| Barium | 1.57 | 1.22 | 0.00 | 4.94 |
| Lead | 0.10 | 0.06 | 0.00 | 0.20 |
| Mercury | 0.005 | 0.003 | 0.00 | 0.01 |

---

## 🤖 Model Details

### Algorithm: XGBoost Classifier
XGBoost (Extreme Gradient Boosting) is an optimized distributed gradient boosting library designed for efficiency and performance.

### Why XGBoost?
- ✅ **High Accuracy** - Superior performance on structured data
- ✅ **Handles Imbalance** - Works well with imbalanced datasets
- ✅ **Fast Training** - Efficient parallel processing
- ✅ **Regularization** - Built-in L1/L2 regularization prevents overfitting
- ✅ **Feature Importance** - Provides insights into parameter significance

### Model Pipeline
```python
1. Load Data → 2. Clean Data → 3. Split (Train/Test) 
   ↓
4. Scale Features → 5. Train XGBoost → 6. Evaluate 
   ↓
7. Save Model (pickle) → 8. Deploy in Flask
```

### Preprocessing
- **StandardScaler:** Normalizes features to have mean=0 and std=1
- **Benefits:** Improves model convergence and prediction accuracy

### Model Files
- `water_xgb_model.pkl` - Serialized XGBoost classifier
- `scaler.pkl` - Fitted StandardScaler object

---

## 🎨 UI/UX Design

### Design Philosophy
The interface follows modern web design principles with a focus on:
- **Visual Appeal** - Gradient backgrounds and smooth animations
- **User-Friendly** - Clear labels and intuitive layout
- **Accessibility** - High contrast and readable fonts
- **Responsiveness** - Adapts to all screen sizes

### Key Design Elements

#### 1. **Animated Background**
- Gradient background (purple to violet)
- Three-layer wave animation
- Smooth, continuous motion

#### 2. **Header Section**
- Pulsing water droplet icon
- Gradient text effect
- Professional subtitle

#### 3. **Info Cards**
- Three feature highlights
- Hover effects with elevation
- Icon-based visual communication

#### 4. **Input Form**
- 2-column grid layout
- 20 labeled input fields
- Focus animations on inputs
- Placeholder values for guidance

#### 5. **Submit Button**
- Gradient background
- Hover elevation effect
- Arrow icon with slide animation
- Loading state support

#### 6. **Results Display**
- Color-coded backgrounds (green/orange)
- Large animated icons
- Bounce-in animation
- Clear typography

### Animations
- **Fade In** - Page load
- **Slide In** - Info cards
- **Pulse** - Header icon
- **Bounce** - Result icon
- **Wave** - Background motion
- **Heartbeat** - Footer icon

---

## 🔌 API Endpoints

### `GET /`
**Description:** Renders the main page with the input form

**Response:** HTML page

---

### `POST /predict`
**Description:** Accepts water quality parameters and returns prediction

**Request Body (Form Data):**
```json
{
  "aluminium": "1.65",
  "ammonia": "9.08",
  "arsenic": "0.04",
  "barium": "2.85",
  "cadmium": "0.007",
  "chloramine": "0.35",
  "chromium": "0.83",
  "copper": "0.17",
  "flouride": "0.05",
  "bacteria": "0.20",
  "viruses": "0.01",
  "lead": "0.054",
  "nitrates": "16.08",
  "nitrites": "1.13",
  "mercury": "0.007",
  "perchlorate": "37.75",
  "radium": "6.78",
  "selenium": "0.08",
  "silver": "0.34",
  "uranium": "0.02"
}
```

**Response:** HTML page with result
- Success: "Safe to Drink 💧" or "Not Safe ❌"
- Error: "Error: Invalid input"

---

## 🔮 Future Enhancements

### Model Improvements
- [ ] Implement SMOTE for handling class imbalance
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Ensemble methods (Random Forest + XGBoost)
- [ ] Feature engineering for better accuracy
- [ ] Cross-validation for robust evaluation

### Application Features
- [ ] User authentication and history tracking
- [ ] Export results as PDF reports
- [ ] Batch prediction from CSV upload
- [ ] Data visualization dashboard
- [ ] Mobile app (React Native/Flutter)

### Technical Enhancements
- [ ] RESTful API with JSON responses
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Unit and integration tests
- [ ] API rate limiting and caching

### UI/UX Improvements
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Accessibility improvements (WCAG 2.1)
- [ ] Progressive Web App (PWA)
- [ ] Real-time parameter validation

---

## 📈 Model Performance

### Evaluation Metrics
To evaluate the model, run the Jupyter notebook `file1.ipynb` which includes:
- **Accuracy Score**
- **Precision, Recall, F1-Score**
- **Confusion Matrix**
- **Classification Report**

### Expected Performance
Given the dataset characteristics:
- High accuracy on majority class (unsafe water)
- Potential for improvement on minority class (safe water)
- Recommended: Use precision-recall metrics for imbalanced data

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Areas for Contribution
- Model optimization
- UI/UX enhancements
- Documentation improvements
- Bug fixes
- Test coverage
- New features

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Bhawya Gulati**

---

## 🙏 Acknowledgments

- Dataset source: Water quality measurements
- XGBoost library developers
- Flask framework contributors
- Font Awesome for icons
- Google Fonts for typography

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/water-quality-prediction/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

---

## 🔗 Links

- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)

---

**⭐ If you find this project useful, please consider giving it a star!**

---

*Last Updated: December 2, 2025*
