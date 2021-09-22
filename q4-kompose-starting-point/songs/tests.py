from django.db import models
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Artist, Song


class SongModelTest(TestCase):
    def test_create_song_success(self):
        song = Song(title="Tempo Perdido", artist="Renato Russo", votes=1)
        song.save()
        self.assertIsNotNone(song.id)

    def test_create_artist_success(self):
        artist = Artist(name="Lenine")
        artist.save()
        self.assertIsNotNone(artist.id)


class TestSongView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.song1_data = {
            "title": "Vento no Litoral",
            "artist": "Renato Russo",
            "votes": 1

        }
        self.song2_data = {
            "title": "Vento no Litoral",
            "artist": "Renato Russo",
            "votes": 2

        }
        self.song3_data = {
            "title": "Vento no Litoral",
            "artist": "",
            "votes": 1

        }
        self.song3_data = {
            "title": "",
            "artist": "Lenine",
            "votes": 1

        }
        self.song3_data = {
            "title": "Cazuza",

        }

    def test_create_song(self):
        # Criando um song
        song = self.client.post(
            "api/songs", self.song1_data, format="json"
        )

        # verificando se o usuário foi inserido corretamente

        self.assertEqual(song.json(), {
            "title": "Vento no Litoral",
            "artist": "Renato Russo",
            "votes": 1

        })

        self.assertEqual(song.status_code, 201)

    def test_wrong_create_song(self):
        # Criando um song
        song = self.client.post(
            "api/songs", self.song3_data, format="json"
        )

        # verificando se o usuário foi inserido corretamente

        self.assertEqual(song.json(), {
            "title": "Vento no Litoral",
            "artist": "",
            "votes": 1

        })

        self.assertEqual(song.status_code, 401)

    def test_list_song(self):
        # Criando um song
        song = self.client.post(
            "api/songs", self.song1_data, format="json"
        )

        # verificando se o usuário foi inserido corretamente

        song_list = self.client.get("api/songs", format="json")

        self.assertListEqual(song_list.json(), [{
            "id": 1,
            "title": "Vento no Litoral",
            "artist": "",
            "votes": 1

        }])
        self.assertEqual(song.status_code, 200)

    def test_put_song(self):
        # Criando um song
        song = self.client.post(
            "api/songs", self.song1_data, format="json"
        )

        # verificando se o usuário foi inserido corretamente

        update_song = self.client.put(
            "api/songs/1", {"title": "Paulo Ricardo"}, format="json")

        self.assertEqual(update_song, 200)

        self.assertDictEqual(update_song.json(), {
            "title": "Paulo Ricardo",
            "artist": "",
            "votes": 1

        })
        self.assertEqual(update_song.status_code, 200)

    def test_delete_song(self):
        # Criando um song
        song = self.client.post(
            "api/songs", self.song1_data, format="json"
        )

        # verificando se o usuário foi inserido corretamente

        delete_song = self.client.delete("api/songs/1", format="json")

        self.assertEqual(delete_song.status_code, 204)

        delete_song = self.client.delete("api/songs/1", format="json")

        self.assertEqual(delete_song.status_code, 404)
