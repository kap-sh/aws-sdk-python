"""Generated from Smithy shape ``com.amazonaws.datazone#FileFormat``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The file format for a notebook export in Amazon SageMaker Unified Studio.</p>"""
FileFormat: TypeAlias = Literal[
    "PDF",
    "IPYNB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PDF",
        "IPYNB",
    )
)


def serialize_json(value: FileFormat) -> str:
    return value


def deserialize_json(data: str) -> FileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileFormat value: {data!r}")
    return cast(FileFormat, data)
