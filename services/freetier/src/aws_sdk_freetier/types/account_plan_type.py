"""Generated from Smithy shape ``com.amazonaws.freetier#AccountPlanType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_freetier.errors import DeserializationError
from aws_sdk_freetier._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccountPlanType: TypeAlias = Literal["FREE", "PAID",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("FREE", "PAID",))


def serialize_aws_json_1_0(value: AccountPlanType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountPlanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountPlanType value: {data!r}")
    return cast(AccountPlanType, data)