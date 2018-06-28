# How to Use
1. make a temp dir like Ted_assignment  
    ```
    $ mkdir Ted_assignment   
    $ cd Ted_assignment
    ```

3. Set virtual envitonment with [Virtualenv](https://virtualenv.pypa.io/en/stable/) or [pipenv](https://github.com/pypa/pipenv)  
    ```
    ex.)  
    $ virtualenv venv  
    $ source vene/bin/activate  
    ```

4. Download source from Git  
    ```
    $ git clone https://github.com/YoungsoonLee/Goleague.git
     ```

5. Install requirements
    ```
    $ pip3 install -r requirements.txt
    ```

6. Change go.sh file
    ```
    $ chmod 0700 go.sh
    ```

7. run server  
    ```
    $ python3 manage.py runserver
    ```

8. Test & Run with bash  
    ```
    $ ./go.sh
    ```

