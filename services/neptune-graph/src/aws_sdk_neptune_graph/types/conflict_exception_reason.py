"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ConflictExceptionReason``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_neptune_graph.errors import DeserializationError
from aws_sdk_neptune_graph._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConflictExceptionReason: TypeAlias = Literal["CONCURRENT_MODIFICATION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONCURRENT_MODIFICATION",))


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)