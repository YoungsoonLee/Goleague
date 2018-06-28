# How to Use
1. make a temp dir like Ted_assignment  
    ```
    $ mkdir Ted_assignment   
    $ cd Ted_assignment
    ```

2. Download source from Git  
    ```
    $ git clone https://github.com/YoungsoonLee/Goleague.git .  
     ```

3. Set virtual envitonment with [Virtualenv](https://virtualenv.pypa.io/en/stable/) or [pipenv](https://github.com/pypa/pipenv)  
    ```
    ex.)  
    $ virtualenv venv  
    $ source venv/bin/activate  
    ```

4. Install requirements
    ```
    $ pip3 install -r requirements.txt
    ```

6. Change go.sh, runserver.sh file
    ```
    $ chmod 0700 go.sh runserver.sh 
    ```

7. run server  
    ```
    $ ./runserver.sh
    ```

8. Test & Run with bash  
    ```
    $ ./go.sh
    ```

