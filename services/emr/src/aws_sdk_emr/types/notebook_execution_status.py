"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecutionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

NotebookExecutionStatus: TypeAlias = Literal[
    "START_PENDING",
    "STARTING",
    "RUNNING",
    "FINISHING",
    "FINISHED",
    "FAILING",
    "FAILED",
    "STOP_PENDING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_PENDING",
        "STARTING",
        "RUNNING",
        "FINISHING",
        "FINISHED",
        "FAILING",
        "FAILED",
        "STOP_PENDING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: NotebookExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookExecutionStatus value: {data!r}")
    return cast(NotebookExecutionStatus, data)
