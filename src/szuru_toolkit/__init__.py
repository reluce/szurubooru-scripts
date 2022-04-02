import sys

from loguru import logger

from .config import Config
from .danbooru import Danbooru
from .gelbooru import Gelbooru
from .sankaku import scrape_sankaku  # noqa F401
from .saucenao import SauceNao
from .szurubooru import Post
from .szurubooru import Szurubooru
from .utils import audit_rating  # noqa F401
from .utils import collect_sources  # noqa F401
from .utils import convert_rating  # noqa F401
from .utils import get_metadata_sankaku  # noqa F401
from .utils import resize_image  # noqa F401
from .utils import sanitize_tags  # noqa F401
from .utils import setup_logger  # noqa F401
from .utils import statistics  # noqa F401


logger.add(
    sink=sys.stderr,
    backtrace=False,
    colorize=True,
    level='ERROR',
    enqueue=True,
    diagnose=False,
    format=''.join(
        '<lr>[{level}]</lr> <lg>[{time:DD.MM.YYYY, HH:mm:ss zz}]</lg> ' '<ly>[{module}.{function}]</ly>: {message}',
    ),
)

config = Config()
if config.auto_tagger['deepbooru_enabled']:
    from .deepbooru import Deepbooru  # noqa F401

__all__ = [
    'Config',
    'Danbooru',
    'Gelbooru',
    'Pixiv',
    'Post',
    'Sankaku',
    'SauceNao',
    'Szurubooru',
]