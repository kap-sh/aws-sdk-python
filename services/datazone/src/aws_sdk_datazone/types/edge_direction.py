"""Generated from Smithy shape ``com.amazonaws.datazone#EdgeDirection``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EdgeDirection: TypeAlias = Literal[
    "UPSTREAM",
    "DOWNSTREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPSTREAM",
        "DOWNSTREAM",
    )
)


def serialize_json(value: EdgeDirection) -> str:
    return value


def deserialize_json(data: str) -> EdgeDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EdgeDirection value: {data!r}")
    return cast(EdgeDirection, data)
