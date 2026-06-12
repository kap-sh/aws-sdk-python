"""Generated from Smithy shape ``com.amazonaws.freetier#Dimension``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_freetier.errors import DeserializationError
from aws_sdk_freetier._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Dimension: TypeAlias = Literal["SERVICE", "OPERATION", "USAGE_TYPE", "REGION", "FREE_TIER_TYPE", "DESCRIPTION", "USAGE_PERCENTAGE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SERVICE", "OPERATION", "USAGE_TYPE", "REGION", "FREE_TIER_TYPE", "DESCRIPTION", "USAGE_PERCENTAGE",))


def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)