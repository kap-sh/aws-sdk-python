"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilterType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailContentFilterType: TypeAlias = Literal["INSULTS", "HATE", "SEXUAL", "VIOLENCE", "MISCONDUCT", "PROMPT_ATTACK",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INSULTS", "HATE", "SEXUAL", "VIOLENCE", "MISCONDUCT", "PROMPT_ATTACK",))


def serialize_json(value: GuardrailContentFilterType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailContentFilterType value: {data!r}")
    return cast(GuardrailContentFilterType, data)