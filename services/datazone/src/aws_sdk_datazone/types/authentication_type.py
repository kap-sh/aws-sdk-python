"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AuthenticationType: TypeAlias = Literal["BASIC", "OAUTH2", "CUSTOM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BASIC", "OAUTH2", "CUSTOM",))


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)