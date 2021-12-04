drop database musicdb;
create database musicdb;

\c musicdb

create table users(userID serial primary key, user_name varchar(25) not null);
create table genre(genre_name text primary key);
create table playlist(plname varchar(20),songID varchar(50),userID int references users(userID)); 
create table writer(writerID serial primary key,writer_name varchar(30) not null);
create table artist(artistID serial primary key,artist_name varchar(30) not null);
create table album(albumID serial primary key,album_name varchar(20),artistID int references artist(artistID));
create table studio(studioID serial primary key,studio_name varchar(20),address varchar(50),albumID int references album(albumID));
create table songs(songID varchar(20) primary key,song_name varchar(20) not null,duration time,genre_name text references genre(genre_name),writerID int references writer(writerID),artistID int references artist(artistID),albumID int references album(albumID));