import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0

    @property
    def channel_id(self):
        """Возвращает id канала. К атрибуту можно обращаться без ()."""
        return f'{self.__name}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('API_KEY')
        # api_key = "AIzaSyDEyhgJHSj9e4vTp9lAvOP3-rPm3hOagzU" #мой ключ
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        items = channel["items"][0]["snippet"]
        statistics = channel["items"][0]["statistics"]
        self.title = items["title"]
        self.description = items["description"]
        self.url = items["thumbnails"]["medium"]["url"]
        self.subscriber_count = statistics["subscriberCount"]
        self.video_count = statistics["videoCount"]
        self.view_count = statistics["viewCount"]
        return channel


    @classmethod
    def get_service(cls):
        apikey: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=apikey)


    def to_json(self, json_fail):
        to_json = {'channel_id': self.__channel_id,
                   'title': self.title,
                   'description': self.description,
                   'url': self.url,
                   'subscriber_count': self.subscriber_count,
                   'video_count': self.video_count,
                   'view_count': self.view_count,
                   }
        with open(json_fail, 'w') as f:
            json.dump(to_json, f, sort_keys=True, indent=2)

    # Домашнее задание 14.1
    def __str__(self):
        return f'{self.title} ({self.url})'


    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count


    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)


    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count


    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count


    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count


    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count


    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

