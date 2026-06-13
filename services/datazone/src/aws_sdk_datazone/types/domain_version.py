"""Generated from Smithy shape ``com.amazonaws.datazone#DomainVersion``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DomainVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1",
        "V2",
    )
)


def serialize_json(value: DomainVersion) -> str:
    return value


def deserialize_json(data: str) -> DomainVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainVersion value: {data!r}")
    return cast(DomainVersion, data)
