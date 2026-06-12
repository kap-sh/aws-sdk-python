"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailWordPolicyAction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailWordPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLOCKED",))


def serialize_json(value: GuardrailWordPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailWordPolicyAction value: {data!r}")
    return cast(GuardrailWordPolicyAction, data)