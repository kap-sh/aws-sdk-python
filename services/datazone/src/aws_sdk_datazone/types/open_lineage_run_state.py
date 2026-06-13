"""Generated from Smithy shape ``com.amazonaws.datazone#OpenLineageRunState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OpenLineageRunState: TypeAlias = Literal[
    "START",
    "RUNNING",
    "COMPLETE",
    "ABORT",
    "FAIL",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START",
        "RUNNING",
        "COMPLETE",
        "ABORT",
        "FAIL",
        "OTHER",
    )
)


def serialize_json(value: OpenLineageRunState) -> str:
    return value


def deserialize_json(data: str) -> OpenLineageRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenLineageRunState value: {data!r}")
    return cast(OpenLineageRunState, data)
