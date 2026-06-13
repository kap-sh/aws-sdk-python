"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExceptionLevel``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExceptionLevel: TypeAlias = Literal["DEBUG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEBUG",))


def serialize_json(value: ExceptionLevel) -> str:
    return value


def deserialize_json(data: str) -> ExceptionLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExceptionLevel value: {data!r}")
    return cast(ExceptionLevel, data)