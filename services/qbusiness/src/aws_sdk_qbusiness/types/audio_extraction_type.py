"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AudioExtractionType: TypeAlias = Literal["TRANSCRIPT", "SUMMARY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TRANSCRIPT", "SUMMARY",))


def serialize_json(value: AudioExtractionType) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioExtractionType value: {data!r}")
    return cast(AudioExtractionType, data)