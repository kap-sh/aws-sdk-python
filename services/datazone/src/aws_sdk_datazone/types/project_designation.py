"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectDesignation``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ProjectDesignation: TypeAlias = Literal[
    "OWNER",
    "CONTRIBUTOR",
    "PROJECT_CATALOG_STEWARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNER",
        "CONTRIBUTOR",
        "PROJECT_CATALOG_STEWARD",
    )
)


def serialize_json(value: ProjectDesignation) -> str:
    return value


def deserialize_json(data: str) -> ProjectDesignation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectDesignation value: {data!r}")
    return cast(ProjectDesignation, data)
