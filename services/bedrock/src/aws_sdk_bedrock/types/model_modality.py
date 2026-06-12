"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelModality``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ModelModality: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "EMBEDDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "IMAGE",
        "EMBEDDING",
    )
)


def serialize_json(value: ModelModality) -> str:
    return value


def deserialize_json(data: str) -> ModelModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelModality value: {data!r}")
    return cast(ModelModality, data)
