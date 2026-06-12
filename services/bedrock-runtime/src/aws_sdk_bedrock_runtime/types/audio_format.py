"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioFormat``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_runtime.errors import DeserializationError
from aws_sdk_bedrock_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AudioFormat: TypeAlias = Literal["mp3", "opus", "wav", "aac", "flac", "mp4", "ogg", "mkv", "mka", "x-aac", "m4a", "mpeg", "mpga", "pcm", "webm",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("mp3", "opus", "wav", "aac", "flac", "mp4", "ogg", "mkv", "mka", "x-aac", "m4a", "mpeg", "mpga", "pcm", "webm",))


def serialize_json(value: AudioFormat) -> str:
    return value


def deserialize_json(data: str) -> AudioFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioFormat value: {data!r}")
    return cast(AudioFormat, data)