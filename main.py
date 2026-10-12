import subprocess

def main():

    print("Running import_data_v2.py...")
    subprocess.run(["python", "src/import_data_v2.py"], check=True)

    print("Running clean_data_v2.py...")
    subprocess.run(["python", "src/clean_data_v2.py"], check=True)

    print("Running polynomial regression model...")
    subprocess.run(["python", "poly_regressor_Python_1.0.0.py"], check=True)

    print("ML pipeline completed successfully")

if __name__ == "__main__":
    main()