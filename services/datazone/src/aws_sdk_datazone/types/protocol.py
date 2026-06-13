"""Generated from Smithy shape ``com.amazonaws.datazone#Protocol``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Protocol: TypeAlias = Literal[
    "ATHENA",
    "GLUE_INTERACTIVE_SESSION",
    "HTTPS",
    "JDBC",
    "LIVY",
    "ODBC",
    "PRISM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATHENA",
        "GLUE_INTERACTIVE_SESSION",
        "HTTPS",
        "JDBC",
        "LIVY",
        "ODBC",
        "PRISM",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
