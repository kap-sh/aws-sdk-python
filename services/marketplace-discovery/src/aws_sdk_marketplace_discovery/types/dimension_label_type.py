"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabelType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_marketplace_discovery.errors import DeserializationError
from aws_sdk_marketplace_discovery._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DimensionLabelType: TypeAlias = Literal["Region", "SagemakerOption",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Region", "SagemakerOption",))


def serialize_json(value: DimensionLabelType) -> str:
    return value


def deserialize_json(data: str) -> DimensionLabelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionLabelType value: {data!r}")
    return cast(DimensionLabelType, data)