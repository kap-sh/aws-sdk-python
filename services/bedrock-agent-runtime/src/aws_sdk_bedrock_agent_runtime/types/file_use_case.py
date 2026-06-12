"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileUseCase``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FileUseCase: TypeAlias = Literal["CODE_INTERPRETER", "CHAT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CODE_INTERPRETER", "CHAT",))


def serialize_json(value: FileUseCase) -> str:
    return value


def deserialize_json(data: str) -> FileUseCase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileUseCase value: {data!r}")
    return cast(FileUseCase, data)