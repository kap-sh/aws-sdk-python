"""Generated from Smithy shape ``com.amazonaws.workspaces#RunningMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RunningMode: TypeAlias = Literal[
    "AUTO_STOP",
    "ALWAYS_ON",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_STOP",
        "ALWAYS_ON",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: RunningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RunningMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RunningMode value: {data!r}")
    return cast(RunningMode, data)
