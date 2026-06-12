"""Generated from Smithy shape ``com.amazonaws.datazone#ComputeEnvironments``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ComputeEnvironments: TypeAlias = Literal["SPARK", "ATHENA", "PYTHON",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SPARK", "ATHENA", "PYTHON",))


def serialize_json(value: ComputeEnvironments) -> str:
    return value


def deserialize_json(data: str) -> ComputeEnvironments:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeEnvironments value: {data!r}")
    return cast(ComputeEnvironments, data)