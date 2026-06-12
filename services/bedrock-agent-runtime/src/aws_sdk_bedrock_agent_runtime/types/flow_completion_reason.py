"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowCompletionReason``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FlowCompletionReason: TypeAlias = Literal["SUCCESS", "INPUT_REQUIRED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUCCESS", "INPUT_REQUIRED",))


def serialize_json(value: FlowCompletionReason) -> str:
    return value


def deserialize_json(data: str) -> FlowCompletionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowCompletionReason value: {data!r}")
    return cast(FlowCompletionReason, data)