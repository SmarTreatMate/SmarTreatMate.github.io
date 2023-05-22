import pandas as pd
import numpy as np
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from multiprocessing import Pool






data_expected_survival = pd.read_csv('expected rate_countypr.csv', low_memory=False)
States = list(data_expected_survival['State'].unique())
state_name = "ak"



def ER_CondPr_calc(Age_State_calc):
    data = pd.DataFrame()
    
    Sex = list(data_expected_survival['Sex'].unique())
    Years = list(data_expected_survival['Year'].unique())
    Races = list(data_expected_survival['ROriginCd'].unique()) 
    
    for sx in Sex:
        for y in Years:
            for r in Races:
                data_expected_survival["ER_CondPr"]= data_expected_survival[(data_expected_survival['State']==state_name.upper())&(data_expected_survival['Age']==Age_State_calc)&(data_expected_survival['Sex']==sx)&(data_expected_survival['Year']==y) & (data_expected_survival['ROriginCd']==r)]["ER_Pr_County_Mul"].sum()                    
                dt = data_expected_survival[(data_expected_survival['State']==state_name.upper())&(data_expected_survival['Age']==Age_State_calc)&(data_expected_survival['Sex']==sx)&(data_expected_survival['Year']==y) & (data_expected_survival['ROriginCd']==r)].copy()
                dt.drop(['ER_Pr_County_Mul'],axis=1,inplace=True)
                dt = dt.iloc[dt['ER_CondPr'].count()-1: , :]
                print("\033[1;33;40m",dt)
                data = data.append(dt)
    return data







if __name__ == '__main__':
    state_name = input("Please select state from the list: {}\n".format(States))
    start = time.time()
    print('\033[1;36;40mThe job has started!')
     
    
    Age_State = list(data_expected_survival['Age'].unique())
    
    print(Age_State)
    
    
    
    p = Pool(processes=20)
    result = p.map(ER_CondPr_calc, Age_State)
   

    p.close()
    p.join()
    end = time.time()
    print('*** \033[1;31;40mThe job has completed in {0} seconds!***'.format(end-start))

    final_data = pd.concat(result)
    
    final_data.to_csv(f'ConditionPr_expected rate_{state_name}.csv',index=False)








