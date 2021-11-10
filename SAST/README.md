# SAST
## Пункт №1
![image](![image](https://user-images.githubusercontent.com/23276203/141159358-67ccb967-04e7-4239-a075-500bb66565f8.png))

## Пункт №2

> $id = $_GET[ 'id' ];

Значение 'id', которое считывается из формы, никакак не обрабатывается и не проверяется перед добавление в запрос, что создает уязвимость для SQL-инъекции.

> $getid  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
> 
> $result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid );
>
> $num = @mysqli_num_rows( $result );

## Пункт №3
Файл task3.php

Для защиты от SQL-инъекции использованы Anti-CSRF токены и проверка вводимого значения id функцией is_numeric().
