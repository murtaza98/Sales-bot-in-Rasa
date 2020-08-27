# Sales Bot in Rasa

## Requirements

- Python 3.7. [Install Python 3.7 on Ubuntu 18.04](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
- Docker

## Installation

1. Install Python. **Please make sure to install Python 3.7. Rasa won't work with any other python version** <br/>

    **Windows** <br/>
    You can install it from [here](https://www.python.org/downloads/windows/)<br/>
    
    **macOS**
    ```bash
    $ brew update
    $ brew install python3.7
    ```
 
    **Linux** 
    ```bash
    $ sudo apt update
    $ sudo apt install python3.7 python3-pip
    ```

2. Install, create and activate a Virtual Environment
    1. Install virtual Environment<br/>
        `python -m pip install --user virtualenv`
    2. Create a virtual environment 
    
        **Linux / macOS**
        ```bash
        $ python3 -m venv ./venv
        ```
     
        **Windows** 
        ```bash
        C:\> python3 -m venv ./venv
        ```
    3. Activate the virtual environment:
    
        **Linux / macOS**
        ```bash
        $ source ./venv/bin/activate
        ```
     
        **Windows** 
        ```bash
        C:\> .\venv\Scripts\activate
        ```

3. Install the required packages from requirements.txt inside this virtual environment:<br/>
    `pip install -r requirements.txt`

4. Install spacy. Ref: [here](https://rasa.com/docs/rasa/user-guide/installation/#dependencies-for-spacy)
    ```bash
    $ pip install rasa[spacy]
    $ python -m spacy download en_core_web_md
    $ python -m spacy link en_core_web_md en
    ```
5. Train the model
    ```bash
    $ rasa train
    ```
    
## Usage Instructions:
1. Activate the environment:
    - **Linux / macOS:** `source venv/bin/activate`
    - **Windows:** `.\venv\Scripts\activate.bat`
2. Open a new terminal and run actions
    - `rasa run actions`
3. Open a new terminal and run duckling which is used for entity extraction
    ```
    docker run -p 8000:8000 rasa/duckling
    ```
3. Lastly, open a new terminal to run rasa <br/>
    `rasa run`
