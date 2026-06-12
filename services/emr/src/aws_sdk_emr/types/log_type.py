"""Generated from Smithy shape ``com.amazonaws.emr#LogType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

LogType: TypeAlias = Literal[
    "system-logs",
    "application-logs",
    "persistent-ui-logs",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "system-logs",
        "application-logs",
        "persistent-ui-logs",
    )
)


def serialize_aws_json_1_1(value: LogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
