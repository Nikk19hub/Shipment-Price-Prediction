import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickled_model=pickle.load(open("/home/shreyas2003/Downloads/Shipment_price/trained_model3.sav",'rb'))


def shipment_price_prdiction(b):
    input_val =b
    final_features = [np.array(input_val)]
    dataframe1 = pd.DataFrame(final_features)

    output = pickled_model.predict(dataframe1 )
    result = "%.2f" % round(output[0], 2)
    return result

def main():
    #title
    st.title("Shipment_Price_Prediction")

    #taking input from user
    Unit_of_Measure=st.text_input("Unit of Measure (per Pack)")
    Line_item_quantity=st.text_input("Line Item Quantity")
    pack_price=st.text_input("Pack Price")
    unit_price=st.text_input("Unit Price")
    freight_cost=st.text_input("Freight Cost (USD $)")
    Line_Item_insurance=st.text_input("Line Item Insurance (USD $)")
    shipment_mode_Ocean=st.text_input("shipment_mode_Ocean")
    shipment_mode_Truck=st.text_input("shipment_mode_Truck")
    shipment_mode_Air=st.text_input("shipment_mode_Air")
    shipment_mode_Air_charter=st.text_input("shipment_mode_Air charter")



    # code for prediction
    price_prediction=""

    # Creating a Button
    if st.button("Predict"):
        price_prediction=shipment_price_prdiction([Unit_of_Measure,Line_item_quantity,pack_price,unit_price,freight_cost,Line_Item_insurance])
    
    st.success(price_prediction)


if __name__=="__main__":
    main()