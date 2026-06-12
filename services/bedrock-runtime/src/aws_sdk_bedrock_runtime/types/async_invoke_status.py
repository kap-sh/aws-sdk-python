"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_runtime.errors import DeserializationError
from aws_sdk_bedrock_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AsyncInvokeStatus: TypeAlias = Literal["InProgress", "Completed", "Failed",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("InProgress", "Completed", "Failed",))


def serialize_json(value: AsyncInvokeStatus) -> str:
    return value


def deserialize_json(data: str) -> AsyncInvokeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AsyncInvokeStatus value: {data!r}")
    return cast(AsyncInvokeStatus, data)