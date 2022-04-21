DESCRIPTION
The code folder consists of different components that ultimately got included in the web app (6_web_server). Different components were built separately and then integrated with the app. Details below:
i. The data exploration was done in Google Colab using Python (project_eda.ipynb in 1_data_exploration folder)
ii. In parallel, a working prototype of the web application was built to visualize how the appl will look like and function (see the .md and .pdf files in 2_wifeframe folder).
iii. The cleaned up data was aggregated in Colab (Team12_Project_DataForTableau.ipynb) and stored in Google Drive. This csv files from Google Drive used in Tableau Desktop to build the dashboard (Descriptive_Dashboard.twbx in 3_descriptive_dashboard folder). This dashboard was then published to the Tableau Publish server. 
iv. The clenaed up data was then used in new notebooks in Colab to build 4 different models. CDC_Explorationipynb, CDC_modeling_2.ipynb and CDC_modeling.ipynb are the files for the 3 models which predict death, hospitalization & ICU admission predictions. The single_target_predict.ipynb file has the code for the 4th model which provides a deterministic health outcome. These models were converted into picked objected to be integrated into the web appl. 
v. The data from these models was stored back into Google drive and aggregated to be used in the Tableau dashboard to showcase model performance metrics (Models_Perf_Dashboard.twbx in 5_models_perf_dashboard folder). 
vi. Lastly, the 6_web_server folder contains the node.js code for the web application, along with code for ML models integration and embedding Tableau dashboards. The app was then deployed on Heroku. 

INSTALLATION
How to install and setup your code

EXECUTION
How to run a demo on your code

DEMO VIDEO
https://youtu.be/da3a9Qu5wwE 