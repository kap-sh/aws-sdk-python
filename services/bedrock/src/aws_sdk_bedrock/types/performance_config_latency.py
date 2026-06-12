"""Generated from Smithy shape ``com.amazonaws.bedrock#PerformanceConfigLatency``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

PerformanceConfigLatency: TypeAlias = Literal[
    "standard",
    "optimized",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "optimized",
    )
)


def serialize_json(value: PerformanceConfigLatency) -> str:
    return value


def deserialize_json(data: str) -> PerformanceConfigLatency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PerformanceConfigLatency value: {data!r}")
    return cast(PerformanceConfigLatency, data)
