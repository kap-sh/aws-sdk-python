"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

PoolStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: PoolStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PoolStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PoolStatus value: {data!r}")
    return cast(PoolStatus, data)
