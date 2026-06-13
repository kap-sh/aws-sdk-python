"""Generated from Smithy shape ``com.amazonaws.datazone#GroupSearchType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GroupSearchType: TypeAlias = Literal[
    "SSO_GROUP",
    "DATAZONE_SSO_GROUP",
    "IAM_ROLE_SESSION_GROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSO_GROUP",
        "DATAZONE_SSO_GROUP",
        "IAM_ROLE_SESSION_GROUP",
    )
)


def serialize_json(value: GroupSearchType) -> str:
    return value


def deserialize_json(data: str) -> GroupSearchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupSearchType value: {data!r}")
    return cast(GroupSearchType, data)
