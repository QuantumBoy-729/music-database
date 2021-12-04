insert into users(user_name) values('Divyansh Raina');
insert into users(user_name) values('Kalash Gollapinni');
insert into users(user_name) values('Harsh Gurawalia');
insert into users(user_name) values('Rekha Agarwal');
insert into users(user_name) values('Vivek Natrajan');
insert into users(user_name) values('Uday Kumar');
insert into users(user_name) values('Rani Singh');
insert into users(user_name) values('Sonal Bhansali');

insert into writer(writer_name) values('Devinder Rajshekhar');
insert into writer(writer_name) values('Amrit Simmons');
insert into writer(writer_name) values('Pranav Menon');
insert into writer(writer_name) values('Vishal Reddy');
insert into writer(writer_name) values('Sanjana Kumar');
insert into writer(writer_name) values('Priya Shetty');
insert into writer(writer_name) values('Fatima Jamal');
insert into writer(writer_name) values('Santosh Singh');

insert into artist(artist_name) values('Manoj Mitra');
insert into artist(artist_name) values('Amrit Simmons');
insert into artist(artist_name) values('Prajwal Reddy');
insert into artist(artist_name) values('Pratheek Shetty');
insert into artist(artist_name) values('Kanan Qatar');
insert into artist(artist_name) values('Ravi Chandra');
insert into artist(artist_name) values('Pratap Kumar');
insert into artist(artist_name) values('Pranav Menon');

insert into album(album_name,artistID) values ('Parklife',1);
insert into album(album_name,artistID) values ('Donda',2);
insert into album(album_name,artistID) values ('Low',3);
insert into album(album_name,artistID) values ('Nevermind',4);
insert into album(album_name,artistID) values ('Days at Home',5);
insert into album(album_name,artistID) values ('Revolver',6);
insert into album(album_name,artistID) values ('Doolittle',7);
insert into album(album_name,artistID) values ('Pet Sounds',8);

insert into studio(studio_name,address,albumID) values('Coke Studio','#40 Nayandahalli Bangalore',1);
insert into studio(studio_name,address,albumID) values('Awaaz Studio','Devatha Plaza',2);
insert into studio(studio_name,address,albumID) values('Decibel Studio','West Park Road',3);
insert into studio(studio_name,address,albumID) values('Studio Ananya','Srirampuram',4);
insert into studio(studio_name,address,albumID) values('Radical Studio','Financial District',5);
insert into studio(studio_name,address,albumID) values('Sound Map Studio','Gachibowli',6);
insert into studio(studio_name,address,albumID) values('Crystal Studio','Taran Square',7);
insert into studio(studio_name,address,albumID) values('Resonance Studio','Bolarabad',8);

insert into genre values('Rock');
insert into genre values('Metal');
insert into genre values('Pop');
insert into genre values('Electro Swing');
insert into genre values('Hip Hop');
insert into genre values('Rap');
insert into genre values('Classical');
insert into genre values('Punk');

insert into songs values('H1','Rock Song','1:50','Rock',1,1,1);
insert into songs values('H2','Rap Song','2:20','Rap',2,2,2);
insert into songs values('En1','Rap Song 2','2:40','Rap',3,3,3);
insert into songs values('H3','Classical Song','1:50','Classical',4,4,4);
insert into songs values('En2','Punk Song','1:30','Punk',5,5,5);
insert into songs values('En3','Electro Swing Song','1:20','Electro Swing',6,6,6);
insert into songs values('H4','Classical Song 2','4:50','Classical',7,7,7);
insert into songs values('H5','Rock Song 2','1:33','Rock',8,8,8);

insert into playlist values('MyPlaylist','H1',1);
insert into playlist values('Workout','H2',2);
insert into playlist values('Jogging','H3',2);
insert into playlist values('Casual','En1',3);
insert into playlist values('MyPlaylist','En1',4);
insert into playlist values('Practice','H1',3);
insert into playlist values('Timepass','En2',5);
insert into playlist values('Study','En3',6);