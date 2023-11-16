'''
WorkFlow: 

1. Data Cleaning --> Handeling missing values, dealing with outliers and correcting data entry errors.

2. Data Integration --> Merging of multiple dataset in one single dataset

3. Data Transformation --> normalization and standardization log or power transformation

4. Feature selection --> Reduce the dimensionality and improve model performance. Correlation analysis, statiscal tests or feature importance analysis

5. Handeling imbalanced data --> Resampleing , oversampling or undersampleing 

6. Handling Text and categorical data --> tokenization, one hot encoder, label encoding 

7. Handeling Date and Time Data --> convert date and time into numerical format
'''
'''
WorkFlow: 

1. Data Cleaning --> Handeling missing values, dealing with outliers and correcting data entry errors.

2. Data Integration --> Merging of multiple dataset in one single dataset

3. Data Transformation --> normalization and standardization log or power transformation

4. Feature selection --> Reduce the dimensionality and improve model performance. Correlation analysis, statiscal tests or feature importance analysis

5. Handeling imbalanced data --> Resampleing , oversampling or undersampleing 

6. Handling Text and categorical data --> tokenization, one hot encoder, label encoding 

7. Handeling Date and Time Data --> convert date and time into numerical format
'''

import streamlit as sl
import pandas as pd

class DatasetReading:
    def get_file(self):

        sl.write("<h1 style='text-align:Center'>Automated Data Pre-Processing</h1>",unsafe_allow_html=True)
        self.file = sl.file_uploader("Upload a file", type=["csv", "xlsx", "xls"])
        self.file_name = sl.text_input(label='Save File With Name As:')

        if self.file is not None:
            if self.file.name.endswith('.csv'):
                self.dataset = pd.read_csv(self.file)
                sl.subheader("Dataset Overview")
                sl.dataframe(self.dataset.head())
                return self.dataset
            elif self.file.name.endswith('.xlsx'):
                self.dataset = pd.read_excel(self.file)
                sl.subheader("Dataset Overview")
                sl.dataframe(self.dataset.head())
                return self.dataset
            else:
                sl.warning("Invalid File Extension or File Not Found")
    
    def get_df_info(self):
        df_columns = self.dataset.columns
        sl.subheader("Dataset Columns")
        sl.table(df_columns)

        sl.subheader("Dataset Missing Values")
        sl.table(self.dataset.isnull().sum())

        sl.subheader("Dataset Column Dtypes")
        sl.table(self.dataset.dtypes)

class DataHandeling(DatasetReading):
    
    def DataEncoding(self):
        sl.subheader("Data Encoding")
        import pandas as pd
        old_dataset = self.dataset
        index_list = []
        for col in old_dataset.columns:
            if old_dataset[col].dtypes == 'object':
                index_list.append(col)
    
        updated_dataset = pd.get_dummies(old_dataset,columns=index_list)
        self.dataset = updated_dataset
        sl.dataframe(self.dataset.head())
    
    def missing_val_imputer(self):
        sl.subheader("Handeling Missing Values")
        updated_dataset = self.dataset
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy='mean')
        updated_dataset = imputer.fit_transform(updated_dataset) 
        self.dataset = pd.DataFrame(updated_dataset,index=self.dataset.index,columns=self.dataset.columns) 
        sl.dataframe(self.dataset.head())  
    
    
    def data_integration(self):
        dataset1_path = sl.text_input("Give Dataset 1 Path:")
        dataset2_path = sl.text_input("Give Dataset 2 Path:")
        dataset1 = pd.read_csv(dataset1_path)
        dataset2 = pd.read_csv(dataset2_path)
        merge_dataset = pd.merge(dataset1,dataset2)
        self.dataset = merge_dataset

    def data_normalization(self):
        sl.subheader("Data Normalization")
        from sklearn.preprocessing import StandardScaler
        raw_dataset = pd.DataFrame(self.dataset)
        print(raw_dataset.head())
        scaler = StandardScaler()
        updated_dataset = scaler.fit_transform(self.dataset)
        self.dataset = pd.DataFrame(updated_dataset,index=self.dataset.index,columns=self.dataset.columns)
        sl.dataframe(self.dataset.head())

    def save_file(self):
        sl.subheader("Processed Dataset")
        sl.dataframe(self.dataset.head())
        if self.file.name.endswith(".csv"):
            sl.download_button(label='Download Processed File',data=self.dataset.to_csv(index=True),file_name=f"{self.file.name.replace('.csv','')} Processed File.csv",key='download_csv')
            return self.dataset
        
        elif '.xlsx' in self.file:
            sl.download_button(label='Download Processed File',data=self.dataset.to_excel(index=True),file_name=f"{self.file.name.replace('.xlsx','')} Processed File.xlsx",key='download_csv')
            return self.dataset
        



user = DataHandeling()
dataset = user.get_file()
user.get_df_info()
user.DataEncoding()
user.missing_val_imputer()
user.data_normalization()
user.save_file()
