"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialLocation``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ApiKeyCredentialLocation: TypeAlias = Literal["HEADER", "QUERY_PARAMETER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HEADER", "QUERY_PARAMETER",))


def serialize_json(value: ApiKeyCredentialLocation) -> str:
    return value


def deserialize_json(data: str) -> ApiKeyCredentialLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiKeyCredentialLocation value: {data!r}")
    return cast(ApiKeyCredentialLocation, data)