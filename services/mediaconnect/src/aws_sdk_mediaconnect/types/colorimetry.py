"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Colorimetry``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Colorimetry: TypeAlias = Literal["BT601", "BT709", "BT2020", "BT2100", "ST2065-1", "ST2065-3", "XYZ",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BT601", "BT709", "BT2020", "BT2100", "ST2065-1", "ST2065-3", "XYZ",))


def serialize_json(value: Colorimetry) -> str:
    return value


def deserialize_json(data: str) -> Colorimetry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Colorimetry value: {data!r}")
    return cast(Colorimetry, data)