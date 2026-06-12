"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ActorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_resiliencehubv2.errors import DeserializationError
from aws_sdk_resiliencehubv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActorType: TypeAlias = Literal["USER", "SYSTEM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USER", "SYSTEM",))


def serialize_json(value: ActorType) -> str:
    return value


def deserialize_json(data: str) -> ActorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActorType value: {data!r}")
    return cast(ActorType, data)