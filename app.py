from flask import Flask, Response
from flask_cors import CORS
import glob
import os
import psycopg2

app = Flask(__name__)
# flask run --host=0.0.0.0 --cert "C:\MEG\Certificate\meg-deploy_polygoninv_local.crt" --key "C:\MEG\Certificate\meg-deploy_polygoninv_local.key"
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Welcome to MEG Visualization Back!</p>"

def read_file_generator(fpath: str):
    try:
        f = open(fpath, 'r')
        while True:
            line = f.readline()
            if not line: 
                break
            
            yield line
    except Exception as e:
        print(e)
    finally:
        f.close()

@app.route("/data/<filename>")
def get_file(filename: str):
    try:
        fpath = f"../data/{filename}"
        return Response(
            read_file_generator(fpath),
            mimetype="text/csv",
            headers={"Content-disposition":
                    f"attachment; filename={filename}"}
        )
    
    except Exception as e:
        return Response(
            None
        )
    
@app.route("/strategy/<strategy>")
def read_strategy(strategy: str):
    try:
        fpath = f"../data/scenarios/{strategy}.csv"
        return Response(
            read_file_generator(fpath),
            mimetype="text/csv",
            headers={"Content-disposition":
                    f"attachment; filename={strategy}.csv"}
        )
    
    except Exception as e:
        return Response(
            None
        )
    

@app.get("/strategies")
def get_strategies_list():
    try:
        strategies = [os.path.splitext(f)[0] for f in os.listdir("../data/scenarios/")] #glob.glob("../data/scenarios/*.csv")]
        return {
            "strategies": strategies
        }
    
    except Exception as e:
        return {
            "error": "Sorry...",
            "message": e
        }
    
@app.get("/scenarios")
def get_scenarios_list():
    try:
        scenarios = ['EquityDown20Pct', 'EquityDown5Pct', 'EquityUp20Pct', 'EquityUp5Pct', 
                     'InterestRateDown25Bps', 'InterestRateDown75Bps', 'InterestRateUp25Bps', 'InterestRateUp75Bps', 
                     'CreditSpreadDown250Bps', 'CreditSpreadDown50Bps', 'CreditSpreadUp250Bps', 'CreditSpreadUp50Bps', 
                     'VolUp4Pct', 'VolDown4Pct', 'VolUp10Pct', 'VolDown10Pct', 
                     'CreditUp25EquityMinus10VolFlat', 'CreditUp25EquityMinus20VolFlat', 'CreditUp25EquityMinus30VolFlat', 'CreditUp50EquityMinus10VolFlat', 
                     'CreditUp50EquityMinus20VolFlat', 'CreditUp50EquityMinus30VolFlat', 'CreditUp100EquityMinus10VolFlat', 'CreditUp100EquityMinus20VolFlat', 
                     'CreditUp100EquityMinus30VolFlat', 'CreditUp25EquityMinus10VolUp25', 'CreditUp25EquityMinus20VolUp25', 'CreditUp25EquityMinus30VolUp25', 
                     'CreditUp50EquityMinus10VolUp25', 'CreditUp50EquityMinus20VolUp25', 'CreditUp50EquityMinus30VolUp25', 'CreditUp100EquityMinus10VolUp25', 
                     'CreditUp100EquityMinus20VolUp25', 'CreditUp100EquityMinus30VolUp25', 'CreditDown25EquityPlus10VolFlat', 'CreditDown25EquityPlus20VolFlat', 
                     'CreditDown25EquityPlus30VolFlat', 'CreditDown100EquityPlus10VolFlat', 'CreditDown100EquityPlus20VolFlat', 'CreditDown100EquityPlus30VolFlat', 
                     'CreditDown50EquityPlus10VolFlat', 'CreditDown50EquityPlus20VolFlat', 'CreditDown50EquityPlus30VolFlat', 
                     'Stagflation', 'FinancialCrisis', 'BullMarket', 'ModerateDeflation', 'InterestRateSpike', 
                     'RatesMinus100bp', 'PerfectStorm', 'PerfectStormVolUp', 'EquityCreditCrash', 
                     'CreditWiden', 'RatesUp', 'EquityCrash', 'BorrowTighten', 
                     'VolUp', 'VolDown', 'RatesDown', 'Basis', 'AEE1', 'AEE2', 'AEE3']
        return {
            "scenarios": scenarios
        }
    
    except Exception as e:
        return {
            "error": "Sorry...",
            "message": e
        }
    

    

@app.get("/convertibles")
def get_convertibles():
    try:
        TABLE_NAME = "risk"
        DB_NAME = "test"
        USERNAME = "test"
        PASSWORD = "test"
        HOST = "test.test.amazonaws.com"
        PORT = 5432
        conn = psycopg2.connect(dbname=DB_NAME, 
            user=USERNAME,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = conn.cursor()
        query = f'''SELECT "Instrument" FROM public.{TABLE_NAME}
            WHERE "Instrument Type" = 'Convertible'
            GROUP BY "Instrument"
            ORDER BY "Instrument"
            ASC
        '''
        cursor.execute(query)

        return cursor.fetchall()
    
    except Exception as e:
        return {
            "error": "Oops!",
            "message": e
        }