"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ChatMode: TypeAlias = Literal["RETRIEVAL_MODE", "CREATOR_MODE", "PLUGIN_MODE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RETRIEVAL_MODE", "CREATOR_MODE", "PLUGIN_MODE",))


def serialize_json(value: ChatMode) -> str:
    return value


def deserialize_json(data: str) -> ChatMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChatMode value: {data!r}")
    return cast(ChatMode, data)