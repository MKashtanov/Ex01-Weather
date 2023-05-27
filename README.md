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

* print_weather_in_plases() - принимает список названий населенных пунктов, выводит в терминал полученную погоду.

* get_weather() - принимает название одного населенного пункта, возвращает текст с погодой в указанном населенном пункте, либо исключение в случае ошибки. 

### Пример запуска скрипта:
#### Пример №1
Запуск  скрипта из коммандной строки.
`> python weather.py`

Результат:
```commandline
Лондон

      \   /     Солнечно
       .-.      19 °C
    ― (   ) ―   ← 4 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      18 °C          │      .-.      +11(10) °C     │
│   ― (   ) ―   ↙ 5-6 м/c      │   ― (   ) ―   ↙ 3-5 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      20 °C          │      .-.      13 °C          │
│   ― (   ) ―   ↙ 3-4 м/c      │   ― (   ) ―   ← 1-2 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │               Пасмурно       │
│      .--.     21 °C          │      .--.     +13(11) °C     │
│   .-(    ).   ↙ 4-5 м/c      │   .-(    ).   ↙ 5-6 м/c      │
│  (___.__)__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Шереметьево

     \  /       Переменная облачность
   _ /"".-.     +22(25) °C
     \_(   ).   ↓ 2 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой ливн…│    \  /       Переменная обл…│
│   ,\_(   ).   22 °C          │  _ /"".-.     17 °C          │
│    /(___(__)  ↓ 3-4 м/c      │    \_(   ).   ↙ 1-3 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │    /(___(__)  10 км          │
│     ‘ ‘ ‘ ‘   0.5 мм | 54%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │  _`/"".-.     Местами дождь  │
│      .-.      +23(25) °C     │   ,\_(   ).   16 °C          │
│   ― (   ) ―   ↓ 1-2 м/c      │    /(___(__)  ↓ 5-9 м/c      │
│      `-’      10 км          │      ‘ ‘ ‘ ‘  9 км           │
│     /   \     0.0 мм | 0%    │     ‘ ‘ ‘ ‘   1.5 мм | 82%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      18 °C          │      .-.      +10(9) °C      │
│   ― (   ) ―   ↘ 6-7 м/c      │   ― (   ) ―   ↘ 3-6 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Череповец

      \   /     Солнечно
       .-.      19 °C
    ― (   ) ―   ↗ 2 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Солнечно       │
│  _ /"".-.     19 °C          │      .-.      14 °C          │
│    \_(   ).   → 4-6 м/c      │   ― (   ) ―   ↓ 3-6 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Солнечно       │
│  _ /"".-.     16 °C          │      .-.      +10(8) °C      │
│    \_(   ).   ↘ 3 м/c        │   ― (   ) ―   ↘ 3-6 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │     \   /     Солнечно       │
│   ,\_(   ).   16 °C          │      .-.      10 °C          │
│    /(___(__)  ↓ 4-6 м/c      │   ― (   ) ―   ↘ 1-3 м/c      │
│      ‘ ‘ ‘ ‘  9 км           │      `-’      10 км          │
│     ‘ ‘ ‘ ‘   0.2 мм | 69%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
```
#### Пример №2
Подключение скрипта как внешнего модуля и получение погоды в Лондоне:

    import weather
    
    print(weather.get_weather('Лондон'))

Результат:

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

#### Пример №3

Подключение скрипта как внешнего модуля и получение погоды в Лондоне, Шереметьево и Череповце.:

    import weather
    
    weather.print_weather_in_places(['Лондон', 'Шереметьево', 'Череповец'])

Результат:

```
Лондон

     \  /       Переменная облачность
   _ /"".-.     +11(9) °C      
     \_(   ).   ↙ 6 м/c        
     /(___(__)  10 км          
                0.0 мм         
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
│   ― (   ) ―   ↙ 3-4 м/c      │   ― (   ) ―   ← 2-3 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Пасмурно       │
│      .-.      20 °C          │      .--.     +12(10) °C     │
│   ― (   ) ―   ↙ 4-5 м/c      │   .-(    ).   ↙ 5-6 м/c      │
│      `-’      10 км          │  (___.__)__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Шереметьево

     \  /       Переменная облачность
   _ /"".-.     19 °C          
     \_(   ).   ↓ 4 м/c        
     /(___(__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │     \   /     Ясно           │
│   ,\_(   ).   21 °C          │      .-.      16 °C          │
│    /(___(__)  ↓ 4-5 м/c      │   ― (   ) ―   ↓ 1-3 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │      `-’      10 км          │
│     ‘ ‘ ‘ ‘   0.1 мм | 66%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │    \  /       Переменная обл…│
│      .-.      +23(25) °C     │  _ /"".-.     16 °C          │
│   ― (   ) ―   ↓ 3 м/c        │    \_(   ).   ↓ 5-10 м/c     │
│      `-’      10 км          │    /(___(__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      19 °C          │      .-.      +10(9) °C      │
│   ― (   ) ―   ↓ 6-7 м/c      │   ― (   ) ―   ↓ 2-5 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Череповец

     \  /       Переменная облачность
   _ /"".-.     16 °C          
     \_(   ).   ↗ 1 м/c        
     /(___(__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤  Пт. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │     \   /     Солнечно       │
│   ,\_(   ).   18 °C          │      .-.      +14(13) °C     │
│    /(___(__)  ↗ 3-5 м/c      │   ― (   ) ―   ↓ 2-4 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │      `-’      10 км          │
│     ‘ ‘ ‘ ‘   0.1 мм | 76%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Сб. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│  _`/"".-.     Местами дождь  │
│  _ /"".-.     17 °C          │   ,\_(   ).   +10(8) °C      │
│    \_(   ).   ↘ 1 м/c        │    /(___(__)  ↘ 3-6 м/c      │
│    /(___(__)  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│               0.0 мм | 0%    │     ‘ ‘ ‘ ‘   0.1 мм | 80%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤  Вс. 28 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      17 °C          │      .-.      11 °C          │
│   ― (   ) ―   ↓ 3-5 м/c      │   ― (   ) ―   ↓ 1-2 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin


Process finished with exit code 0
```

### Цель проекта

Урок 1 курса Devman 
