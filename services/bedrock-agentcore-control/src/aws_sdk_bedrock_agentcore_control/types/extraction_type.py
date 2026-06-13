"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The extraction type for a metadata field, determining how the value is obtained during memory processing.</p>"""
ExtractionType: TypeAlias = Literal["LLM_INFERRED", "STRICTLY_CONSISTENT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LLM_INFERRED", "STRICTLY_CONSISTENT",))


def serialize_json(value: ExtractionType) -> str:
    return value


def deserialize_json(data: str) -> ExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExtractionType value: {data!r}")
    return cast(ExtractionType, data)