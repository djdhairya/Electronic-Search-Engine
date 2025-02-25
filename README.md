# Electronic Search Engine

## Overview

The **Electronic Search Engine** is a recommendation system built using Streamlit that helps users find similar electronic products based on their selection. The system leverages a precomputed similarity matrix to provide recommendations.

## Features

- User-friendly Streamlit interface.
- Provides top 10 similar products based on selected electronic items.
- Displays product names and images for better visualization.
- Uses a precomputed similarity matrix to ensure quick recommendations.
- Handles image validation before displaying recommendations.

## Installation

### Prerequisites


Ensure you have the following installed:

- Python 3.x
- Required Python libraries: `streamlit`, `pandas`, `numpy`, `nltk`, `scikit-learn`, `pickle`, `PIL`, `requests`

### Setup

1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install streamlit pandas numpy nltk scikit-learn pillow requests
   ```
3. Place the `data.pkl` and `similarity.pkl` files inside the `model` directory.

## Usage

Run the application using Streamlit:

```bash
streamlit run app.py
```

## File Structure

```
Electronic Search Engine/
│── model/
│   ├── data.pkl
│   ├── similarity.pkl
│── data/
│   ├── All Electronics.csv
│── app.py
│── test.py
│── electronic_search.ipynb
│── README.md
```

- `app.py`: Main Streamlit application for product search and recommendations.
- `test.py`: Additional script for testing image validity before displaying recommendations.
- `model/data.pkl`: Pickle file containing electronic product data.
- `model/similarity.pkl`: Precomputed similarity matrix for recommendations.
- `model_training.py`: Script for processing data, generating similarity matrix, and saving model files.

## How It Works

1. **Data Preprocessing**:

   - Load electronic product data from CSV.
   - Clean and preprocess data (handle missing values, remove duplicates, tokenize text, apply stemming, etc.).
   - Convert text data into a numerical format using Count Vectorization.
   - Compute similarity scores using Cosine Similarity.

2. **Recommendation System**:

   - User selects a product from the dropdown.
   - The application fetches the top 10 most similar products based on precomputed similarity.
   - The recommended products are displayed with images and names.

## Example Output

- **User selects**: *iPhone 12*
- **Recommended products**:
  - iPhone 12 Pro
  - iPhone 11
  - Samsung Galaxy S21
  - etc.

## Future Enhancements

- Implement a search bar for quick product lookup.
- Improve similarity calculations using deep learning models.
- Add a feedback mechanism to improve recommendations.

## License

This project is open-source under the MIT License.

![Screenshot 2025-02-25 234705](https://github.com/user-attachments/assets/25c962ae-b462-48d2-86e7-becbdd46d83f)
