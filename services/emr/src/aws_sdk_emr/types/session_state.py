"""Generated from Smithy shape ``com.amazonaws.emr#SessionState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SessionState: TypeAlias = Literal[
    "SUBMITTED",
    "STARTING",
    "STARTED",
    "IDLE",
    "BUSY",
    "TERMINATING",
    "TERMINATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "STARTING",
        "STARTED",
        "IDLE",
        "BUSY",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionState value: {data!r}")
    return cast(SessionState, data)
