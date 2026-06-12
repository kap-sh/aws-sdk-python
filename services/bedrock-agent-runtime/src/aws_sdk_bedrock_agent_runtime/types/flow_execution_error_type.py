"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionErrorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FlowExecutionErrorType: TypeAlias = Literal["ExecutionTimedOut",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ExecutionTimedOut",))


def serialize_json(value: FlowExecutionErrorType) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionErrorType value: {data!r}")
    return cast(FlowExecutionErrorType, data)