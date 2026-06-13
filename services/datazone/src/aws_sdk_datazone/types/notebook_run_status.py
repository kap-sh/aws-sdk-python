"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The status of a notebook run in Amazon SageMaker Unified Studio.</p>"""
NotebookRunStatus: TypeAlias = Literal[
    "QUEUED",
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: NotebookRunStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookRunStatus value: {data!r}")
    return cast(NotebookRunStatus, data)
