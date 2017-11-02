"""
Django settings for hok8_bu7 project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.決策樹仔問題.閩南語決策樹仔 import 閩南語決策樹仔
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
from 臺灣言語工具.語音合成.決策樹仔問題.客家話決策樹仔 import 客家話決策樹仔
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.語音合成.決策樹仔問題.官話決策樹仔 import 官話決策樹仔
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音相容教會羅馬字音標 import 臺灣閩南語羅馬字拼音相容教會羅馬字音標
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音
from 臺灣言語工具.音標系統.客話綜合標音 import 客話綜合標音
from 臺灣言語工具.音標系統.官話綜合標音 import 官話綜合標音
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 原住民族語言書寫系統秀姑巒阿美語
from 臺灣言語工具.語音合成.南島語語音標仔轉換 import 南島語語音標仔轉換
from 臺灣言語工具.語音合成.決策樹仔問題.秀姑巒阿美語決策樹仔 import 秀姑巒阿美語決策樹仔
from 臺灣言語工具.語音合成.漢語語音標仔轉換 import 漢語語音標仔轉換
from 臺灣言語工具.語音合成.閩南語音韻規則 import 閩南語音韻規則
from 臺灣言語工具.音標系統.SaySiyat.賽夏 import 賽夏
from 臺灣言語工具.語音合成.決策樹仔問題.賽夏決策樹仔 import 賽夏決策樹仔
from 臺灣言語工具.音標系統.Atayal.賽考利克 import 賽考利克
from 臺灣言語工具.語音合成.決策樹仔問題.南島語決策樹仔 import 南島語決策樹仔
from 臺灣言語工具.音標系統.Bunun.Bubukun import Bubukun

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y+i8k(!#=%npz7^1^&2cit6gbv&()_c=tls$(z4q)vh%2dd9^v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '臺灣言語資料庫',
    '臺灣言語服務',
    'corsheaders',
    '匯入到臺灣言語資料庫',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
CORS_ORIGIN_REGEX_WHITELIST = ('^.*$', )
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'hok8_bu7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hok8_bu7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "資料庫影音檔案")
MEDIA_URL = "/資料庫影音檔案/"

HOK8_BU7_SIAT4_TING7 = {
    '閩南語': {
        '語族': '漢語',
        '音標系統': 臺灣閩南語羅馬字拼音,
        '解析拼音': 臺灣閩南語羅馬字拼音相容教會羅馬字音標,
        '字綜合標音': 閩南語綜合標音,
        '音韻規則': 閩南語音韻規則,
        '語音標仔轉換': 漢語語音標仔轉換,
        '決策樹仔': 閩南語決策樹仔,
        '辨識設定': {
              '腳本資料夾': os.path.join(BASE_DIR, 'kaldi/egs/taiwanese/s5c'),
              '腳本': '服務來試.sh',
              '語料資料夾': 'data',
              '模型資料夾': 'tri5.2',
              '圖資料夾': 'graph_sp',
              '結果檔名': '7.0.0.txt',
        },
    },
    '臺語': {
        '語族': '漢語',
        '音標系統': 臺灣閩南語羅馬字拼音,
        '解析拼音': 臺灣閩南語羅馬字拼音相容教會羅馬字音標,
        '字綜合標音': 閩南語綜合標音,
        '音韻規則': 閩南語音韻規則,
        '語音標仔轉換': 漢語語音標仔轉換,
        '決策樹仔': 閩南語決策樹仔,
        '辨識設定': {
              '腳本資料夾': os.path.join(BASE_DIR, 'kaldi/egs/taiwanese/s5c'),
              '腳本': '服務來試nnet3.sh',
              '語料資料夾': 'data',
              '模型資料夾': 'nnet3_clain',
              '圖資料夾': 'graph_sp',
              '結果檔名': '7.0.0.txt',
        },
    },
    '官話': {
        '語族': '漢語',
        '音標系統': 官話注音符號,
        '字綜合標音': 官話綜合標音,
        '語音標仔轉換': 漢語語音標仔轉換,
        '決策樹仔': 官話決策樹仔,
    },
}

for 客語 in ['四縣腔', '海陸腔', '大埔腔', '饒平腔', '詔安腔', '南四縣腔']:
    HOK8_BU7_SIAT4_TING7[客語] = {
        '語族': '漢語',
        '音標系統': 臺灣客家話拼音,
        '字綜合標音': 客話綜合標音,
        '語音標仔轉換': 漢語語音標仔轉換,
        '決策樹仔': 客家話決策樹仔,
    }

for 族語 in [
    '霧台魯凱語', '萬山魯凱語', '東魯凱語', '茂林魯凱語', '大武魯凱語', '多納魯凱語',
    '建和卑南語', '知本卑南語', '南王卑南語', '初鹿卑南語',
    '拉阿魯哇語', '德路固語',  '卡那卡那富語',
    '中排灣語', '北排灣語', '南排灣語', '東排灣語',
    'Pangcah', '海岸阿美語', '恆春阿美語', '馬蘭阿美語', '中部阿美語', '北部阿美語',
    '雅美語', '噶瑪蘭語',
    '都達語', '邵語', '阿里山鄒語', '太魯閣語',
    '撒奇萊雅語', '德固達雅語',
]:
    HOK8_BU7_SIAT4_TING7[族語] = {
        '語族': '南島語',
        '音標系統': 原住民族語言書寫系統秀姑巒阿美語,
        '語音標仔轉換': 南島語語音標仔轉換,
        '決策樹仔': 秀姑巒阿美語決策樹仔,
    }

for 族語 in ['SaySiyat', '賽夏語', ]:
    HOK8_BU7_SIAT4_TING7[族語] = {
        '語族': '南島語',
        '音標系統': 賽夏,
        '語音標仔轉換': 南島語語音標仔轉換,
        '決策樹仔': 賽夏決策樹仔,
    }
for 族語 in [
    'Atayal', '泰雅語',
    '賽考利克泰雅語', '澤敖利泰雅語', '宜蘭澤敖利泰雅語', '萬大泰雅語', '四季泰雅語', '汶水泰雅語',
]:
    HOK8_BU7_SIAT4_TING7[族語] = {
        '語族': '南島語',
        '音標系統': 賽考利克,
        '語音標仔轉換': 南島語語音標仔轉換,
        '決策樹仔': 南島語決策樹仔(賽考利克),
    }
for 族語 in [
    'Bunun', '布農語',
    'Bubukun',
    '丹群布農語', '卓群布農語', '卡群布農語', '巒群布農語', '郡群布農語',
]:
    HOK8_BU7_SIAT4_TING7[族語] = {
        '語族': '南島語',
        '音標系統': Bubukun,
        '語音標仔轉換': 南島語語音標仔轉換,
        '決策樹仔': 南島語決策樹仔(Bubukun),
    }

# 上傳的音檔上大1G，限制予nginx做
DATA_UPLOAD_MAX_MEMORY_SIZE = 1073741824
# For better celery performance
CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = TIME_ZONE

try:
    from hok8_bu7.local import SECRET_KEY, DEBUG, DATABASES
except ImportError:
    SECRET_KEY, DEBUG, DATABASES
