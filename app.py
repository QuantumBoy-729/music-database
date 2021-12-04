from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
db = SQLAlchemy(app)
pl = {}

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(10), nullable = False)
    password = db.Column(db.String(10), nullable = False)
    playlists = db.relationship('Playlist', backref='user')

genre_types = db.Table('genre_types', 
db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    playlist_name = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    song_name = db.Column(db.String(50), nullable = False)
    file_path = db.Column(db.String(100), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    playlists = db.relationship('Playlist', backref='song')
    genres = db.relationship('Genre', secondary=genre_types, backref=db.backref('songs', lazy='dynamic'))

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(50), nullable = False)
    songs = db.relationship('Song', backref='artist_song')
    albums = db.relationship('Album', backref='artist_album')

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(20))
    

class Album(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    album_name = db.Column(db.String(50), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    songs = db.relationship('Song', backref='album')


@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']

        users = User.query.all()
        
        for user in users:
            if user.username == user_name and user.password == password:
                return redirect(f'/home/{user.id}')
    

    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        new_user = User(username = user_name, password = password)
        db.session.add(new_user)
        # db.session.commit()
        # new_playlist = Playlist(playlist_name = str(new_user.username)+"'s Playlist", user_id = new_user.id)
        # db.session.add(new_playlist)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('signup.html')

@app.route('/home/<int:id>')
def home(id):
    songs = Song.query.all()
    user = User.query.get_or_404(id)
    return render_template('home.html', songs = songs, user = user)

@app.route('/playlist/<int:id>', methods = ['GET', 'POST'])
def playlist(id):
    user = User.query.get_or_404(id)
    songs_in_playlist = db.session.query(Song).join(Playlist).join(User).filter(Playlist.user_id == id).all() 
    if request.method == 'POST':
        song_id = request.form['song_id']
        new_playlist = Playlist(playlist_name = str(user.username) + "'s Playlist", user_id = id, song_id = song_id)
        db.session.add(new_playlist)
        db.session.commit()
        songs_in_playlist = db.session.query(Song).join(Playlist).join(User).filter(Playlist.user_id == id).all() 
        return render_template('playlist.html', playlist = songs_in_playlist, user = user)
    else:
        return render_template('playlist.html', playlist = songs_in_playlist, user = user)

@app.route('/playlist/delete', methods = ['POST', 'GET'])
def remove_from_playlist():
    if request.method == 'POST':
        song_id = request.form['song_id']
        user_id = request.form['user_id']
        to_delete = db.session.query(Playlist).filter_by(song_id = song_id).filter_by(user_id = user_id).first()
        db.session.delete(to_delete)
        db.session.commit()
        return redirect(f'/playlist/{user_id}')

@app.route('/details/<int:id>')
def display_details(id):
    song = Song.query.get_or_404(id)
    genre_type = db.session.query(genre_types).filter_by(song_id = id).first()
    genre = Genre.query.get_or_404(genre_type.genre_id)
    artist_id = song.artist_id
    album_id = song.album_id
    artist = Artist.query.get_or_404(artist_id)
    album = Album.query.get_or_404(album_id)
    return render_template('details.html', artist = artist, song = song, album = album, genre = genre)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_song():
    if request.method == 'POST':
        file = request.files['file']
        song_name = request.form['song_name']
        artist_name = request.form['artist_name']
        album_name = request.form['album_name']
        new_artist = Artist(artist_name = artist_name)
        db.session.add(new_artist)
        db.session.commit()
        new_album = Album(album_name = album_name, artist_id = new_artist.id)
        db.session.add(new_album)
        db.session.commit()
        new_song = Song(song_name = song_name, artist_id = new_artist.id, album_id = new_album.id, file_path = f'/static/music/{file.filename}')
        db.session.add(new_song)
        db.session.commit()
        file.save(os.path.join("static\\music", file.filename))
        return render_template('upload.html')
    return render_template('upload.html')

@app.route('/deleteSong', methods = ['GET', 'POST'])
def delete_song():
    song_to_delete_id = request.form["to_delete"]
    user_id = request.form['u_id']
    song_to_delete = Song.query.get_or_404(song_to_delete_id)
    db.session.delete(song_to_delete)
    db.session.commit()
    return redirect(f'/home/{user_id}')

if __name__ == "__main__":
    app.run(debug=True)