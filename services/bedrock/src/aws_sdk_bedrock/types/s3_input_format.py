"""Generated from Smithy shape ``com.amazonaws.bedrock#S3InputFormat``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

S3InputFormat: TypeAlias = Literal["JSONL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JSONL",))


def serialize_json(value: S3InputFormat) -> str:
    return value


def deserialize_json(data: str) -> S3InputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3InputFormat value: {data!r}")
    return cast(S3InputFormat, data)
