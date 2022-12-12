# Forecasting New York Taxi Demand

New York City has almost 14,000 yellow taxis. This means it's important to know where and when taxi demand is high, to maximize customer satistfaction and revenue. 

This project builds a time series model to forecast taxi demand in Lower Manhattan.

## Data

The NYC Taxi & Limousine Commission website contains data on taxi rides in New York:

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Data from October 2021 to September 2022 was used. This gave 12 months of data.

The website supplies data for each month in its own file. To avoid duplicates, records from other months were removed from each file e.g., Novemeber records were removed from the October file. 

Pick-up times were rounded to the nearest hour. The data was summarised to get the number of rides per hour. This gave 8.765 observations.

## Methodology

Data from October 2021 to June 2022 was used to train the model, and the rest was used as an unseen test set. 

The Prophet forecasting model, developed by the Facebook data science team, was used. More details on the model can be found here:

https://peerj.com/preprints/3190/

## Results

![image](https://user-images.githubusercontent.com/63146102/207087491-dfb4ba35-91da-4666-824d-6facb3f57c2b.png)

This graph shows the true hourly values, the fitted model and the predictions on the unseen test set.

The model seems like a poor fit, given that it fits values less than zero which isn't possible. 

## Conclusion

This model would need to be improved to be used to accurately forecast taxi demand. This could be done by testing different hyperparameters of the model or trying a poisson time series model.






