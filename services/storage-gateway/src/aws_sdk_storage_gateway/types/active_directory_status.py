"""Generated from Smithy shape ``com.amazonaws.storagegateway#ActiveDirectoryStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActiveDirectoryStatus: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DETACHED",
    "JOINED",
    "JOINING",
    "NETWORK_ERROR",
    "TIMEOUT",
    "UNKNOWN_ERROR",
    "INSUFFICIENT_PERMISSIONS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "DETACHED",
        "JOINED",
        "JOINING",
        "NETWORK_ERROR",
        "TIMEOUT",
        "UNKNOWN_ERROR",
        "INSUFFICIENT_PERMISSIONS",
    )
)


def serialize_aws_json_1_1(value: ActiveDirectoryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveDirectoryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActiveDirectoryStatus value: {data!r}")
    return cast(ActiveDirectoryStatus, data)
