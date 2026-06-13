"""Generated from Smithy shape ``com.amazonaws.datazone#TargetEntityType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

TargetEntityType: TypeAlias = Literal[
    "DOMAIN_UNIT",
    "ENVIRONMENT_BLUEPRINT_CONFIGURATION",
    "ENVIRONMENT_PROFILE",
    "ASSET_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOMAIN_UNIT",
        "ENVIRONMENT_BLUEPRINT_CONFIGURATION",
        "ENVIRONMENT_PROFILE",
        "ASSET_TYPE",
    )
)


def serialize_json(value: TargetEntityType) -> str:
    return value


def deserialize_json(data: str) -> TargetEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetEntityType value: {data!r}")
    return cast(TargetEntityType, data)
