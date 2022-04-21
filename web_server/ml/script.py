import pandas as pd
import sys
import os
import numpy as np
import joblib

def main():
    state = sys.argv[1]
    county = sys.argv[2]
    ageGroup = sys.argv[3]
    race = sys.argv[4]
    curretStatus = sys.argv[5]
    sex = sys.argv[6]
    
    testPath = os.path.join(sys.argv[7], 'test.csv')
    countyPath = os.path.join(sys.argv[7], 'county_lookup_table.csv')
    
    deathMlModelPath = os.path.join(sys.argv[7], 'RF_death.joblib')
    icuMlModelPath = os.path.join(sys.argv[7], 'RF_icu.joblib')
    hospMlModelPath = os.path.join(sys.argv[7], 'RF_hosp.joblib')

    encoding1MlModelPath = os.path.join(sys.argv[7], 'encoding1.joblib')
    # encoding2MlModelPath = os.path.join(sys.argv[7], 'encoding2.joblib')

    df_test = pd.read_csv(testPath)
    
    df_test['current_status_' + curretStatus] = 1
    df_test['race_' + race] = 1
    df_test['sex_' + sex] = 1
    if (ageGroup == '65_plus'):
        df_test["age_group_65+_years"] = 1
    else:
        df_test['age_group_' + ageGroup] = 1
    df_test['res_state_' + state] = 1
    
    df_county_lookup = pd.read_csv(countyPath)
    selected_county = df_county_lookup[df_county_lookup['Recip_County'] == county]

    if (selected_county.shape[0] == 1):
        # print(selected_county)
        df_test['county_metro_yn'] = int(selected_county['Metro_status'])
        df_test['county_SVI'] = int(selected_county['SVI_CTGY'])
        df_test['county_census_2019'] = int(selected_county['Census2019'])
    else:
        df_test['county_metro_yn'] = 1
        df_test['county_SVI'] = 2
        df_test['county_census_2019'] = 5150233

    deathMlModel = joblib.load(deathMlModelPath)
    print(int(deathMlModel.predict_proba([df_test.iloc[0]])[0][0] * 100), '%')
    del deathMlModel

    icuMlModel = joblib.load(icuMlModelPath)
    print(int(icuMlModel.predict_proba([df_test.iloc[0]])[0][0] * 100), '%')
    del icuMlModel

    hospMlModel = joblib.load(hospMlModelPath)
    print(int(hospMlModel.predict_proba([df_test.iloc[0]])[0][0] * 100), '%')
    del hospMlModel
    
    encoding1MlModel = joblib.load(encoding1MlModelPath)
    print(encoding1MlModel.predict(df_test.iloc[:,0:72]))
    del encoding1MlModel



if __name__ == "__main__":
    main()


# Deterministic health outcomes