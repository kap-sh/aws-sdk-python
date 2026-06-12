"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ConnectionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConnectionStatus: TypeAlias = Literal["CONNECTED", "DISCONNECTED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONNECTED", "DISCONNECTED",))


def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)