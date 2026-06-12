"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceBundleState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

WorkspaceBundleState: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: WorkspaceBundleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceBundleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceBundleState value: {data!r}")
    return cast(WorkspaceBundleState, data)
