"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizerType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AuthorizerType: TypeAlias = Literal["CUSTOM_JWT", "AWS_IAM", "NONE", "AUTHENTICATE_ONLY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CUSTOM_JWT", "AWS_IAM", "NONE", "AUTHENTICATE_ONLY",))


def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerType value: {data!r}")
    return cast(AuthorizerType, data)