"""Generated from Smithy shape ``com.amazonaws.bedrock#RetrieveAndGenerateType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RetrieveAndGenerateType: TypeAlias = Literal[
    "KNOWLEDGE_BASE",
    "EXTERNAL_SOURCES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KNOWLEDGE_BASE",
        "EXTERNAL_SOURCES",
    )
)


def serialize_json(value: RetrieveAndGenerateType) -> str:
    return value


def deserialize_json(data: str) -> RetrieveAndGenerateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrieveAndGenerateType value: {data!r}")
    return cast(RetrieveAndGenerateType, data)
