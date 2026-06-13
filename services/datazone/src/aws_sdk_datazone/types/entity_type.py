"""Generated from Smithy shape ``com.amazonaws.datazone#EntityType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EntityType: TypeAlias = Literal[
    "ASSET",
    "DATA_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "DATA_PRODUCT",
    )
)


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
