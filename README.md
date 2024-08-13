# Shipment-Price-Prediction
<br>
Shipment price predictive forecasting uses statistical techniques and machine learning to predict future prices based on historical data. It assists in understanding past trends, enhancing decision-making for cash flow, risk assessment, capacity planning, and meeting customer demands in the supply chain.
<br>
<br>
Problem Statement:
<br>
To provide a methodological approach to analyze the ongoing trends and predicting the future price of shipment packages based on various factors which affect the pricing. This prediction is to be done using the machine learning models.
<br>
<br>
After studying the data, we checked how well three models could predict outcomes by looking at Mean Square Error (MSE). This MSE tells us how close the predictions are to the real outcomes, where lower values mean the models are more accurate.
For the linear regression model, we discovered the MSE to be 7464564098.525732. This means that, typically, the difference between the predicted and actual values squared is quite large for this model.
<br>
<br>
After that, we looked at the random forest model, and its MSE was 2938398750.6968093. This number is smaller than the MSE of the linear regression model, which shows that the random forest model did a better job at predicting accurately.
Finally, we studied the LGBM regressor model, and its MSE was the lowest among the three models, at 2821495076.7183814.
This means that the LGBM regressor model did better than both the linear regression and random forest models at reducing prediction errors.
<br>
<br>
We also found the R square value for each model, and the values of the R square are given below:-
<br>
a. Linear Regression: 0.9433245648252444
<br>
b. Random Forest Regressor: 0.9776899192351244
<br>
c. LGBM Regressor: 0.9785775218477891
