"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilterName``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CacheReportFilterName: TypeAlias = Literal[
    "UploadState",
    "UploadFailureReason",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UploadState",
        "UploadFailureReason",
    )
)


def serialize_aws_json_1_1(value: CacheReportFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheReportFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheReportFilterName value: {data!r}")
    return cast(CacheReportFilterName, data)
