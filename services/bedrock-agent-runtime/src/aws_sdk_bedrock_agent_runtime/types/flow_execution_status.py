"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FlowExecutionStatus: TypeAlias = Literal["Running", "Succeeded", "Failed", "TimedOut", "Aborted",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Running", "Succeeded", "Failed", "TimedOut", "Aborted",))


def serialize_json(value: FlowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionStatus value: {data!r}")
    return cast(FlowExecutionStatus, data)