# Goal: 
We want to help  commercial crab farmers to known the right age of their  crabs. This will help  them decide if and when to harvest the crabs. Beyond a certain age, there is negligible growth in crab's physical characteristics and hence, it is important to time the harvesting to reduce cost and increase profit. 

Also, we want to understand the different physical feature changes with age.

For this project we spent less time doing EDA. This is because data was so clean an we did not need to delve deep to pick up trends.
After EDA, we went into choosing the machine learing model for this problem.
Since we were predicting the age of crabs, we used a regression model(Supervised Learning).
Our loss metrics were mean_absolute_error,mean_squared_error,root_mean_squared_error	and r2.
Our best performing model was the Xgboostreg.

We then went ahead to deploy model using fast api and Docker, we hosted this on our huggingface  space .
Also we continued and built a streamlit app.

link to huggingface space :https://kwamenas-crab-predictor-fast-api.hf.space

Take aways: We realised that the Length of a crab has less correlation with tha age of the crab.
Same with the weight of the crab.
The three most important features that have a high correlation with the age of the crab in pir dataset are:
1. Shell Weight
2. Height
3. Shuck weight.

Feel free to explore on this and i'm open for any questions and collabprations
Email: niiadjei.sowah68@gmail.com
