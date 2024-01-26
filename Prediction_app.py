import streamlit as st
import pandas as pd
import joblib

# Define encoding functions
def code_Residence_Type(residence_type):
    return 0 if residence_type == 'flat' else (1 if residence_type == 'shared room' else 2)

def code_yes_no(value):
    return 1 if value == 'Yes' else 0

def main():

    # Load the best model from the pickle file
    loaded_best_model = joblib.load('best_model.pkl')

    # Streamlit App
    st.title('Haldia House Rent Prediction App')

    # Create input widgets for each feature
    user_input = {
        'Residence_Type': st.selectbox("Select Residence Type:", ('flat', 'shared room', 'single room')),
        'Residence_Score': st.number_input("Give Residence Score:", 0, 5, step=1),
        'Attached_bathroom': st.selectbox("Attached Bathroom:", ('Yes', 'No')),
        'attached_kitchens': st.selectbox("Attached Kitchen:", ('Yes', 'No')),
        'avl_shoopingmall': st.selectbox("Available Shopping Mall:", ('Yes', 'No')),
        'avl_transport_facility_colllege': st.selectbox("Available Transport Facility:", ('Yes', 'No')),
        'avl_medical': st.selectbox("Available Medical Facility:", ('Yes', 'No')),
        'avl_fooding': st.number_input("Number of canteen available:", 1, 5, step=1),
        'avl_transport_market_time': st.selectbox("Minimum Duration to reach Market(in minutes):", (5, 10, 15)),
        'transport_time': st.selectbox("Minimum Duration to reach College(in minutes):", (10, 5, 15, 20, 30)),
        'avl_play_ground': st.selectbox("Available Playground:", ('Yes', 'No')),
    }

    # Process user input
    user_input['Residence_Type'] = code_Residence_Type(user_input['Residence_Type'])
    user_input['Attached_bathroom'] = code_yes_no(user_input['Attached_bathroom'])
    user_input['attached_kitchens'] = code_yes_no(user_input['attached_kitchens'])
    user_input['avl_shoopingmall'] = code_yes_no(user_input['avl_shoopingmall'])
    user_input['avl_transport_facility_colllege'] = code_yes_no(user_input['avl_transport_facility_colllege'])
    user_input['avl_medical'] = code_yes_no(user_input['avl_medical'])
    user_input['avl_play_ground'] = code_yes_no(user_input['avl_play_ground'])

    # Create a Submit button
    submit_button = st.button('Submit')

    # Check if the button is clicked
    if submit_button:
        try:
            # Convert user input to DataFrame
            user_input_df = pd.DataFrame([user_input])

            # Predict the house rent based on user input
            prediction = loaded_best_model.predict(user_input_df)[0]
            prediction = str(prediction)

            # Display the prediction in the middle of the display
            st.subheader('Predicted House Rent:')
            st.success(f"Prediction: Rs. {prediction}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
