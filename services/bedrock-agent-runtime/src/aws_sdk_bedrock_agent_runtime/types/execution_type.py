"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExecutionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExecutionType: TypeAlias = Literal["LAMBDA", "RETURN_CONTROL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAMBDA", "RETURN_CONTROL",))


def serialize_json(value: ExecutionType) -> str:
    return value


def deserialize_json(data: str) -> ExecutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionType value: {data!r}")
    return cast(ExecutionType, data)