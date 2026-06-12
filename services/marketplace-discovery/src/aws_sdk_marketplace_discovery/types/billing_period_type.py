"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#BillingPeriodType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_marketplace_discovery.errors import DeserializationError
from aws_sdk_marketplace_discovery._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BillingPeriodType: TypeAlias = Literal["Monthly",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Monthly",))


def serialize_json(value: BillingPeriodType) -> str:
    return value


def deserialize_json(data: str) -> BillingPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingPeriodType value: {data!r}")
    return cast(BillingPeriodType, data)