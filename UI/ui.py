import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model and label encoder
rf_classifier = joblib.load('/Users/bhushan/Desktop/venv/Chennai Water Quality 02/Model(s)/Random Forest Joblib/rf_classifier_model.joblib')
label_encoder = joblib.load('/Users/bhushan/Desktop/venv/Chennai Water Quality 02/Model(s)/Random Forest Joblib/label_encoder.joblib')

# Create the main window
root = tk.Tk()
root.title("Water Quality Prediction")
root.geometry("1300x300")  # Adjusted window size to fit two columns

# Labels for the features
feature_names = [
    'D.O. mg/L', 'pH', 'Conductivity m mhos/cm', 'BOD at 27C mg/L',
    'Fecal Coliform MPN/100ml', 'Turbidity NTU', 'Total Alkalinity mg/L',
    'Total Kjeldahl Nitrogen mg/L', 'Magnesium as Mg++ mg/L',
    'TotalPhosphate\nmg/L', 'Fluoride mg/L'
]

# Create a frame to hold the input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Create a dictionary to hold the entry fields
entries = {}

# Arrange the labels and entry fields in two columns
for i, feature in enumerate(feature_names):
    label = tk.Label(input_frame, text=feature)
    entry = tk.Entry(input_frame)

    # Place in two columns (0 and 1) with 5 rows each
    row = i % 5
    col = i // 5
    label.grid(row=row, column=col * 2, padx=10, pady=5, sticky="e")  # Labels in even columns
    entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5, sticky="w")  # Entries in odd columns

    # Store the entry widget in the dictionary
    entries[feature] = entry


# Function to get input values, make prediction, and display result
def predict():
    try:
        # Collect values from the entry fields
        input_features = []
        for feature in feature_names:
            value = float(entries[feature].get())
            input_features.append(value)

        # Convert input to a DataFrame (to match model input format)
        input_df = pd.DataFrame([input_features], columns=feature_names)

        # Make prediction using the loaded model
        prediction = rf_classifier.predict(input_df)
        predicted_class = label_encoder.inverse_transform(prediction)[0]

        # Show the result in a message box
        messagebox.showinfo("Prediction Result", f"Predicted DBU Class: {predicted_class}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")


# Add a submit button centered below the input fields
submit_button = tk.Button(root, text="Submit", command=predict)
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()