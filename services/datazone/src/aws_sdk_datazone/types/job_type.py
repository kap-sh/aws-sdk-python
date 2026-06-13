"""Generated from Smithy shape ``com.amazonaws.datazone#JobType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

JobType: TypeAlias = Literal["LINEAGE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINEAGE",))


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
