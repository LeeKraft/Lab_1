# SDL_Lab_2
## 1 Пункт
![image](https://user-images.githubusercontent.com/22303711/139029583-a95f6c48-eaba-47fd-ac52-e3b10fe848d3.png)

## 2 Пункт

> $id = $_GET[ 'id' ];

Значение 'id', считываемое из формы, никаким образов не обрабатывается и не проверяется перед добавление его [значения] в запрос

> $getid  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
> 
> $result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid );
>
> $num = @mysqli_num_rows( $result );

что позволяет выполнить SQL-инъекцию

## 3 Пункт
Файл lab2.php

Для защиты от SQL-инъекции использованы Anti-CSRF токены и проверка вводимого значения id функцией is_numeric().
