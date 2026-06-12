"""Generated from Smithy shape ``com.amazonaws.bedrock#RerankingMetadataSelectionMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RerankingMetadataSelectionMode: TypeAlias = Literal[
    "SELECTIVE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECTIVE",
        "ALL",
    )
)


def serialize_json(value: RerankingMetadataSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RerankingMetadataSelectionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RerankingMetadataSelectionMode value: {data!r}"
        )
    return cast(RerankingMetadataSelectionMode, data)
