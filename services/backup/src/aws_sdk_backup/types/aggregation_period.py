"""Generated from Smithy shape ``com.amazonaws.backup#AggregationPeriod``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_backup.errors import DeserializationError
from aws_sdk_backup._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AggregationPeriod: TypeAlias = Literal["ONE_DAY", "SEVEN_DAYS", "FOURTEEN_DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ONE_DAY", "SEVEN_DAYS", "FOURTEEN_DAYS",))


def serialize_json(value: AggregationPeriod) -> str:
    return value


def deserialize_json(data: str) -> AggregationPeriod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregationPeriod value: {data!r}")
    return cast(AggregationPeriod, data)