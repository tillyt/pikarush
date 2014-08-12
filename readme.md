# For the Future YFNCC of pika

First, you should fork my repo and then clone it locally on your computer

You will have to change a little bit in src/pikarush/calendar.clj and src-cljs/pikarush/main.cljs to have the correct dates

Next, take a Google Drive spreadsheet wih the rush events on it in the correct format, specified by events/csv2edn.py, and download the spreadsheet as a .csv file. Now, move the csv file to events, and navigate to that directory. In terminal, run: `python csv2edn.py rushevents.csv` and my script will convert it to the correct format for you. 

Now, you need to install leiningen to compile the Clojure code

1. Install [leiningen](http://leiningen.org/)
2. From the command line, do: `lein run`

3. To spit out a new version of the js, do:

  ```
  lein cljsbuild once
  ```
or  `lein cljsbuild auto`

`auto` lets you change things and have the results recompile automatically!
Hooray!
