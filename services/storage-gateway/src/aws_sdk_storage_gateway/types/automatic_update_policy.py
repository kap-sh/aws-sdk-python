"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticUpdatePolicy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomaticUpdatePolicy: TypeAlias = Literal[
    "ALL_VERSIONS",
    "EMERGENCY_VERSIONS_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_VERSIONS",
        "EMERGENCY_VERSIONS_ONLY",
    )
)


def serialize_aws_json_1_1(value: AutomaticUpdatePolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomaticUpdatePolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomaticUpdatePolicy value: {data!r}")
    return cast(AutomaticUpdatePolicy, data)
