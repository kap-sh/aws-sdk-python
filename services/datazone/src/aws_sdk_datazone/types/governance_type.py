"""Generated from Smithy shape ``com.amazonaws.datazone#GovernanceType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GovernanceType: TypeAlias = Literal[
    "AWS_MANAGED",
    "USER_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_MANAGED",
        "USER_MANAGED",
    )
)


def serialize_json(value: GovernanceType) -> str:
    return value


def deserialize_json(data: str) -> GovernanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GovernanceType value: {data!r}")
    return cast(GovernanceType, data)
