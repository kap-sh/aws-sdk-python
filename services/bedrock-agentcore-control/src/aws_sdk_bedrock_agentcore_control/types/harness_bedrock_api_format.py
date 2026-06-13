"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessBedrockApiFormat``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

HarnessBedrockApiFormat: TypeAlias = Literal["converse_stream", "responses", "chat_completions",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("converse_stream", "responses", "chat_completions",))


def serialize_json(value: HarnessBedrockApiFormat) -> str:
    return value


def deserialize_json(data: str) -> HarnessBedrockApiFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessBedrockApiFormat value: {data!r}")
    return cast(HarnessBedrockApiFormat, data)