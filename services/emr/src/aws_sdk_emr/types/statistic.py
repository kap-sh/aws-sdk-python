"""Generated from Smithy shape ``com.amazonaws.emr#Statistic``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Statistic: TypeAlias = Literal[
    "SAMPLE_COUNT",
    "AVERAGE",
    "SUM",
    "MINIMUM",
    "MAXIMUM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAMPLE_COUNT",
        "AVERAGE",
        "SUM",
        "MINIMUM",
        "MAXIMUM",
    )
)


def serialize_aws_json_1_1(value: Statistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Statistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {data!r}")
    return cast(Statistic, data)
