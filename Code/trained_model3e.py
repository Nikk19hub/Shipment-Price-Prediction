import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickled_model=pickle.load(open('/home/shreyas2003/Downloads/Shipment_price/regr_trained.sav','rb'))


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
    shipment = [ "Air", "Air_Charter", "Ocean", "Truck"]
    shipment_mode = st.selectbox("Select shipment mode", shipment)
    shipment_temp = [0,0,0,0]
    shipment_temp[shipment.index(shipment_mode)] = 1


    # code for prediction
    price_prediction=""

    # Creating a Button
    if st.button("Predict"):
        lis = [Unit_of_Measure,Line_item_quantity,pack_price,unit_price,freight_cost,Line_Item_insurance]
        for items in shipment_temp:
            lis.append(items)
        price_prediction=shipment_price_prdiction(lis)
        print(lis)
    st.success(price_prediction)


if __name__=="__main__":
    main()