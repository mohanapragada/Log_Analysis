# Log_Analysis
# Designed by Mohana
display the  top three articles


Logs Analysis Project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Project content

This project consists for the following files are:

* LogAnalysis_Udacity.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* newsdata.sql - database file
* OutPut.JPG

## Required Tools

1. Python
2. Vagrant
3. VirtualBox
4. Postgresql

## Installation

There are some dependancies and a few instructions on how to run the application.

## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal

## How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/Log_Analysis_Udacity`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/Log_Analysis_Udacity
`.

  6. In terminal Change directory to `vagrant/Log_Analysis_Udacity` and look around with ls.

  7. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
  8. Load the Virtual Tables or Create Views in Local Data Base
  
  ```
    $ psql -d news -f views.sql
  ```
   9. Run newsdata.py using:
  ```
    $ python LogAnalysis_Udacity.py.py
  ```
  Note: queries will take sometime to execute 


