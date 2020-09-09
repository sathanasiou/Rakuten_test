### Simple MAC Address maping 

In order to run the API follow the steps bellow :   
1. Pull the repository. 
2. From repoditory folder run : 
    ```
    docker-compose up -d
    ```
    Using -d flag will help so the program runs in the background.
3. Inside docker-compose there is a maping between container's and localhost port, both are 5000. In order to use the API you can do it either from inside the container using : 
    ```
    docker exec -it -u root rakuten_test_container /bin/bash
    ```
    From inside the container run :   
        ```
        curl http://127.0.0.1:5000/find_company/<mac-address>
        ```   
    mac-address is a parameter for the request and there user should provide the desired parameter to search.

    Example:   
        ```
        root@fb53eebb6914:/rakuten_test# curl http://127.0.0.1:5000/find_company/a4:83:e7:ab:4d:31  
        [
        "company:Apple, Inc", 
        200
        ]
        ```
4. If user wants to run it from localhost, especially for Mac should use : 
    ```
    docker exec -it rakuten_test_container curl http://localhost:5000/find_company/<mac-address>
    ```

There are also other ways to implement that API for example using http.client python, the way I implemented it is using python and flask framework. It is not the optimal or the way I would recommend for production use due to security risks, also another security risk is due to authetication been inside the request uri of macadress.io API. Data are returned in a json format including company name and response status code.# Rakuten_test
