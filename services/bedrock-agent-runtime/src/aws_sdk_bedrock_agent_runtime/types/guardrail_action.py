"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailAction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailAction: TypeAlias = Literal["INTERVENED", "NONE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERVENED", "NONE",))


def serialize_json(value: GuardrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailAction value: {data!r}")
    return cast(GuardrailAction, data)