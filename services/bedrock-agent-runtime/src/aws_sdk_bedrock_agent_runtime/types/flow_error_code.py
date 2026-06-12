"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowErrorCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FlowErrorCode: TypeAlias = Literal["VALIDATION", "INTERNAL_SERVER", "NODE_EXECUTION_FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VALIDATION", "INTERNAL_SERVER", "NODE_EXECUTION_FAILED",))


def serialize_json(value: FlowErrorCode) -> str:
    return value


def deserialize_json(data: str) -> FlowErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowErrorCode value: {data!r}")
    return cast(FlowErrorCode, data)