from atp import __version__

from atp.client import Client
from atp.config import VOICE2VEC, AV2VEC


def test_version():
    assert __version__ == '0.2.0'


def test_import():
    APPId = ""
    APIKey = ""
    APISecret = ""
    model = AV2VEC
    cli = Client(model, api_key=APIKey, api_secret=APISecret,app_id=APPId)
    res = cli.get_feature(audio = "./resource/input/audio/test.wav", video="./resource/input/video/test.MOV")
    print(res)
if __name__ == '__main__':
    test_import()
