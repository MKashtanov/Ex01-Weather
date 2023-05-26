# Получение погоды в терминале

Проект реализует получение погоды с сайта [wttr.in](https://wttr.in/) и вывод ее в текстовом виде. 

## Как использовать

Python3 должен быть уже установлен.
Также понадобится установить пакет **requests** 

```
pip install requests
```
Модуль запущенный отдельно, получает погоду в Лондоне, Шереметьево и Череповце.

### Методы

* get_weather_in_plases() - принимает список названий населенных пунктов, выводит в терминал полученную погоду.

* get_weather() - принимает название одного населенного пункта, возвращает текст с погодой в указанном населенном пункте, либо текст с сообщением об ошибке. 

### Пример вывода

получение погоды в Лондоне:

```commandline
get_weather('Лондон')
```
результат:

```
Лондон

     \  /       Переменная облачность
   _ /"".-.     +15(14) °C     
     \_(   ).   ↙ 3 м/c        
     /(___(__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤  Чт. 25 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     20 °C          │      .-.      +13(12) °C     │
│    \_(   ).   ↙ 3-4 м/c      │   ― (   ) ―   ← 2-3 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      18 °C          │      .-.      +11(9) °C      │
│   ― (   ) ―   ↙ 5-6 м/c      │   ― (   ) ―   ↙ 3-5 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      19 °C          │      .-.      +13(12) °C     │
│   ― (   ) ―   ↙ 4 м/c        │   ― (   ) ―   ← 1-3 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
```

### Цель проекта

Урок 1 курса Devman 
