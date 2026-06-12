"""Generated from Smithy shape ``com.amazonaws.workspaces#TargetWorkspaceState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

TargetWorkspaceState: TypeAlias = Literal[
    "AVAILABLE",
    "ADMIN_MAINTENANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "ADMIN_MAINTENANCE",
    )
)


def serialize_aws_json_1_1(value: TargetWorkspaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetWorkspaceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetWorkspaceState value: {data!r}")
    return cast(TargetWorkspaceState, data)
