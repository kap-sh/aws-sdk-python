"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeStorageClass``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

TapeStorageClass: TypeAlias = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEEP_ARCHIVE",
        "GLACIER",
    )
)


def serialize_aws_json_1_1(value: TapeStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TapeStorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TapeStorageClass value: {data!r}")
    return cast(TapeStorageClass, data)
