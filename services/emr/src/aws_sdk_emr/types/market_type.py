"""Generated from Smithy shape ``com.amazonaws.emr#MarketType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MarketType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SPOT",
    )
)


def serialize_aws_json_1_1(value: MarketType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MarketType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketType value: {data!r}")
    return cast(MarketType, data)
