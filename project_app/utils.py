import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class LoanPre():
    def __init__(self,credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,purpose):
        
        self.credit_policy=credit_policy
        self.int_rate=int_rate
        self.installment=installment
        self.log_annual_inc=log_annual_inc
        self.dti=dti
        self.fico=fico
        self.days_with_cr_line=days_with_cr_line
        self.revol_bal=revol_bal
        self.revol_util=revol_util
        self.inq_last_6mths=inq_last_6mths
        self.delinq_2yrs=delinq_2yrs
        self.pub_rec=pub_rec
        self.purpose="purpose_"+purpose
  
    
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)     

    def get_predicted_charges(self):
        
        self.load_models()  
        purpose_index=list(self.json_data["columns"]).index(self.purpose)
        
        test_array=np.zeros(len(self.json_data["columns"]))
       
    
        test_array[0]=self.credit_policy
        test_array[1]=self.int_rate
        test_array[2]=self.installment
        test_array[3]=self.log_annual_inc
        test_array[4]=self.dti
        test_array[5]=self.fico
        test_array[6]=self.days_with_cr_line
        test_array[7]=self.revol_bal
        test_array[8]=self.revol_util
        test_array[9]=self.inq_last_6mths
        test_array[10]=self.delinq_2yrs
        test_array[11]=self.pub_rec
        test_array[purpose_index]=1
        print("test array -->\n",test_array)
        charges=round(self.model.predict([test_array])[0],2) 
        return charges
if __name__== "__main__":
    credit_policy=1.000000
    int_rate=0.118900
    installment=829.100000
    log_annual_inc=11.350407
    dti=19.480000
    fico=737.000000
    days_with_cr_line=5639.958333
    revol_bal=28854.000000
    revol_util=52.100000
    inq_last_6mths=0.000000
    delinq_2yrs=0.000000
    pub_rec=0.000000
    purpose="credit_card"
    
    
    lon_pri=LoanPre(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,purpose)
    premium=lon_pri.get_predicted_charges()
    print("Predicted Prices:",premium,"/-rs")        


