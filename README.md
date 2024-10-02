# House-Price-Prediction-in-Yemen
This Python program aims to predict house prices in Yemen using machine learning techniques. It leverages a Random Forest Regressor model trained on a dataset of house features and corresponding prices. The program provides a user-friendly interface for entering house information and obtaining estimated prices.



**Installation:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shaher2001/house-price-prediction
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**Usage:**

1. **Run the program:**
   ```bash
   python house.py
   ```
2. **Enter house information:**
   - Input values for:
     - Area (square meters)
     - Number of rooms
     - Number of bathrooms
     - Number of halls
     - Number of kitchens
     - Number of streets
     - Street area 1
     - Street area 2
     - Location (choose from available options)
3. **Click "Predict Price":**
   - The estimated house price will be displayed.

**Data:**

- The program uses a dataset of house features and corresponding prices.
- You can replace the sample data with your own dataset by modifying the `X` and `y` variables in the code.

**Model:**

- A Random Forest Regressor model is used for price prediction.
- You can experiment with different models or adjust the model's hyperparameters to improve performance.

**Features:**

- User-friendly graphical interface
- Handles missing data gracefully
- Provides estimated price range
- Considers cultural and economic factors specific to Yemen

**Limitations:**

- The accuracy of the predictions depends on the quality and quantity of the training data.
- The model may not be able to accurately predict prices for houses with unique features or in unusual locations.

**Future Improvements:**

- Expand the dataset to include more diverse house features and locations.
- Explore other machine learning algorithms for better performance.
- Implement a web-based interface for wider accessibility.
- Incorporate real-time data updates for more accurate predictions.

**Contributing:**

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

**License:**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

**Additional Notes:**

- Remember to replace `your-username` with your actual GitHub username in the clone command.
- Ensure you have the required Python libraries installed (e.g., `tkinter`, `sklearn`, `numpy`).
- Customize the README to reflect your specific project details and goals.

I hope this README file is helpful and provides a clear overview of your program!
