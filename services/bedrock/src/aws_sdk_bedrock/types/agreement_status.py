"""Generated from Smithy shape ``com.amazonaws.bedrock#AgreementStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AgreementStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "NOT_AVAILABLE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "NOT_AVAILABLE",
        "ERROR",
    )
)


def serialize_json(value: AgreementStatus) -> str:
    return value


def deserialize_json(data: str) -> AgreementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgreementStatus value: {data!r}")
    return cast(AgreementStatus, data)
