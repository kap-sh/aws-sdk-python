"""Generated from Smithy shape ``com.amazonaws.emr#AdjustmentType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AdjustmentType: TypeAlias = Literal[
    "CHANGE_IN_CAPACITY",
    "PERCENT_CHANGE_IN_CAPACITY",
    "EXACT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHANGE_IN_CAPACITY",
        "PERCENT_CHANGE_IN_CAPACITY",
        "EXACT_CAPACITY",
    )
)


def serialize_aws_json_1_1(value: AdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdjustmentType value: {data!r}")
    return cast(AdjustmentType, data)
