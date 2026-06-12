"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowExecutionState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The type of instance.</p>"""
JobFlowExecutionState: TypeAlias = Literal[
    "STARTING",
    "BOOTSTRAPPING",
    "RUNNING",
    "WAITING",
    "SHUTTING_DOWN",
    "TERMINATED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "BOOTSTRAPPING",
        "RUNNING",
        "WAITING",
        "SHUTTING_DOWN",
        "TERMINATED",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: JobFlowExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobFlowExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobFlowExecutionState value: {data!r}")
    return cast(JobFlowExecutionState, data)
