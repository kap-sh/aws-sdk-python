"""Generated from Smithy shape ``com.amazonaws.bedrock#ProvisionedModelStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ProvisionedModelStatus: TypeAlias = Literal[
    "Creating",
    "InService",
    "Updating",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "InService",
        "Updating",
        "Failed",
    )
)


def serialize_json(value: ProvisionedModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisionedModelStatus value: {data!r}")
    return cast(ProvisionedModelStatus, data)
