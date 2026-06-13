"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DeploymentMode: TypeAlias = Literal[
    "ON_CREATE",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_CREATE",
        "ON_DEMAND",
    )
)


def serialize_json(value: DeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> DeploymentMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentMode value: {data!r}")
    return cast(DeploymentMode, data)
