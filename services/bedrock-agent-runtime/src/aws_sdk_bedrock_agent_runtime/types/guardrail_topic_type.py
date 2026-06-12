"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopicType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailTopicType: TypeAlias = Literal["DENY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DENY",))


def serialize_json(value: GuardrailTopicType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTopicType value: {data!r}")
    return cast(GuardrailTopicType, data)