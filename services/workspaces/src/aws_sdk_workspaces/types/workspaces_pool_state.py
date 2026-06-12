"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

WorkspacesPoolState: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: WorkspacesPoolState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspacesPoolState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspacesPoolState value: {data!r}")
    return cast(WorkspacesPoolState, data)
