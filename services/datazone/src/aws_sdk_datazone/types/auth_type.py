"""Generated from Smithy shape ``com.amazonaws.datazone#AuthType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AuthType: TypeAlias = Literal["IAM_IDC", "DISABLED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IAM_IDC", "DISABLED",))


def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthType value: {data!r}")
    return cast(AuthType, data)