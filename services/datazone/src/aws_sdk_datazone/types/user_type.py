"""Generated from Smithy shape ``com.amazonaws.datazone#UserType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

UserType: TypeAlias = Literal[
    "IAM_USER",
    "IAM_ROLE",
    "SSO_USER",
    "IAM_ROLE_SESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_USER",
        "IAM_ROLE",
        "SSO_USER",
        "IAM_ROLE_SESSION",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
