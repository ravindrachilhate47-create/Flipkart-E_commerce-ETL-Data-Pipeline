import pandas as pd
import logging 
from pathlib import Path


logging.basicConfig(level=logging.INFO)

input_files= Path("not files")
output_files= Path("flipkart_pipeline_clean.CSV")


class flipkart_jone:
    def __init__(self,input_files,output_files):
        self.input_files=input_files
        self.output_files=output_files

    def extract(self):
        logging.info("Reding CSV files ")
        df=pd.read_csv(self.input_files)
        return df
    
    def file_info(self,df):
        logging.info(" Basic info in Files  ")  
        print("TOP 5 rows \n",df.head(5))
        print("data shape \n",df.shape)
        print("basic info \n",df.info())
        print("check value \n",df.isna().sum())
        print("check duplicateds \n",df.duplicated().sum())
        print("Drop duplicates \n",df.drop_duplicates().sum())

        return df 

    def transform(self,df):
        logging.info(" Transforming data  ")
        df['Order ID']=df['Order ID']
        df['Product Name'] = df['Product Name'].astype(str).str.strip()
        df['Category']=df['Category'].str.strip()
        df['Price (INR)']= df['Price (INR)'].fillna(0)
        return df

    def load(self,df):
        logging.info("Loading a files on PC")
        self.output_files.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        df.to_csv(self.output_files,index=False)
        print(f"File saved at: {self.output_files}")

    def run(self):
        try:
            df=self.extract()
            df=self.file_info(df)
            df=self.transform(df)
            self.load(df)
            logging.info("pipeline complited succesfully")
        except Exception as e:
          logging.error(f"piprline failde{e}")


pipeline=flipkart_jone(
    input_files,
    output_files
)
pipeline.run()
            

        
        
