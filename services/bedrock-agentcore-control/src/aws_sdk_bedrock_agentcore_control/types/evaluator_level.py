"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorLevel``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EvaluatorLevel: TypeAlias = Literal["TOOL_CALL", "TRACE", "SESSION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TOOL_CALL", "TRACE", "SESSION",))


def serialize_json(value: EvaluatorLevel) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluatorLevel value: {data!r}")
    return cast(EvaluatorLevel, data)