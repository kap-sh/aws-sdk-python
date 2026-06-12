"""Generated from Smithy shape ``com.amazonaws.freetier#CurrencyCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_freetier.errors import DeserializationError
from aws_sdk_freetier._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CurrencyCode: TypeAlias = Literal["USD",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_aws_json_1_0(value: CurrencyCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)