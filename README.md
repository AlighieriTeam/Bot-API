# Alighieri Bot API

**Jest to repozytorium skierowane do użytkownika chcącego podłączyć bota do gry na naszej platformie *Alighieri*.**

## Struktura repozytorium
```
.
├── API
│   ├── Client
│   │   ├── app.py
│   │   └── requirements.txt
│   └── User
└── README.md
```

Repozytorium składa się z folderu pod nazwą API oraz podfolderów Client i User: 
* **Client** zawiera pliki, które służą do połączenia się z platformą Alighieri.
    * **app.py** jest łącznikiem między kodem napisanym przez użytkownika, a stroną na której trwa rozgrywka.
    * **requirements.txt** zawieraja informacje o wszystkich importach potrzebnych do uruchomienia plików w programie klienta.
> Nie należy zmieniać plików w folderze **Client**.
* **User** jest przestrzenią gdzie użytkownik powinien umieścić swojego bota.

## Schemat użytkowania
Przed uruchomieniem programu:
1.  Należy pobrać potrzebne importy do plików pythonowych wywołując komendę:

```shell
> pip install -r requirements.txt
```

2. Aby program działał poprawnie trzeba podać token udostępniony użytkownikowi ze strony pokoju i wpisać go w odpowiednie miejsce.

> miejsce

3. Po wpisaniu tych komend powinien zostać uruchomiony poprawnie client i połączenie zostać nawiązane.

```shell
> python app.py
```

4. Następnie użytkownik powinien uruchomić swój program napisany w dowolnym języku umieszczony w folderze user.

## Opis działania relacji pomiędzy programem użytkownika a clientem
Program użytkownika powinien wysyłać na wskazany adres ip jsona odpowiedniego dla danej gry zawierającego następny ruch bota. 
Client następnie przesyła jsona na stronę i czeka na kolejnego. 
W tym samym czasie udostępnia lokalizację pod którą znajduje się json z danymi ze strony dotyczącymi aktualnego stanu rozgrywki.

### Pliki JSON

#### Stan gry udostępniany użytkownikowi 
```json
{
  "is_game_active": bool, 
  "game_state": [
    "map": [
      [],
      [],
      ...,
      []
    ],
    "avail_actions": [] // for pacman: [up, down, left, right], for pong: [left, right]
  ]
}
```

#### Kolejny ruch botawysyłany przez użytkownika:
```json
{
  "is_game_active": bool,
  "move": str // for pacman: [up, down, left, right], for pong: [left, right], one of this ofc
}
```

---
# Alighieri Bot API

**This is a repository aimed at the user who wants to connect a bot to play on our site *Alighieri*.** 

##  Repository structure
```
.
├── API
│   ├── Client
│   │   ├── app.py
│   │   └── requirements.txt
│   └── User
└── README.md
```

Repository consists of a folder named API and 2 subfolders Client and User:
* **Client** contains files that are used to connect to the site.
  * **app.py** is the link between the code written by the user and the page on which the game is running.
  * **requirements.txt** contains information about all the imports needed to run the files in the client program.
> Files in **Client** folder shouldn't be modified.
* **User** is space where user can store theirs bot`s files.

## Usage scheme
Before running the program:
1. You need to download the necessary imports to the python files by calling the command:

```shell
> pip install -r requirements.txt
```

2. In order for the program to run correctly you need to provide the token provided to the user from the room page and enter it in the appropriate place.

> place

3. After typing these commands, the client should run correctly and the connection should be established.

```shell
> python app.py
```

4. Then the user should run his program written in any language placed in the user folder.

## Relationship between the user program and the client
The user program should send to the specified ip address json appropriate for the game containing information about the bot`s movement. 
The client then sends the json to the page and waits for the next one. 
At the same time, it provides the location under which the json is located with data from the page about the current state of the game.

### JSON files

#### Game state available to the user 

```json
{
  "is_game_active": bool, 
  "game_state": [
    "map": [
      [],
      [],
      ...,
      []
    ],
    "avail_actions": [] // for pacman: [up, down, left, right], for pong: [left, right]
  ]
}
```

#### Bot`s next move sent by the user:
```json
{
  "is_game_active": bool,
  "move": str // for pacman: [up, down, left, right], for pong: [left, right], one of this ofc
}
```
