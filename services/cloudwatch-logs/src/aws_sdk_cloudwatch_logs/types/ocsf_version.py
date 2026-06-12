"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OCSFVersion``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OCSFVersion: TypeAlias = Literal[
    "V1.1",
    "V1.5",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1.1",
        "V1.5",
    )
)


def serialize_aws_json_1_1(value: OCSFVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OCSFVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OCSFVersion value: {data!r}")
    return cast(OCSFVersion, data)
