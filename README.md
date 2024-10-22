# Tiny Dataset Notebook

> **If you do not have a subscription JetBrains DataSpell you can use PyCharm Community for free and install the jupyter package to run notebooks in the browser. See instructions below.**

Create a new virtual environment if so desired: `python3 -m venv <your env name>` then `source 

Next run pip install -r requirements.txt inside your env.

Create an .env file in the root project directory and supply `OPENAI_API_KEY=` with the proper key.

The database file is included with the repo but if needed, run `python main.py` in the src directory to create a new database.

This main file can be used to create databases from other CSV files. 


# For Pycharm Community

- Install PyCharm Community and clone the project
- Ensure you are in the proper env and run `pip install jupyter`
- Once installed run `jupyter notbook` from the console, this opens a browser and you can then run the notebook connected to the project.
