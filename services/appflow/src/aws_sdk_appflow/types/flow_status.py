"""Generated from Smithy shape ``com.amazonaws.appflow#FlowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

FlowStatus: TypeAlias = Literal[
    "Active",
    "Deprecated",
    "Deleted",
    "Draft",
    "Errored",
    "Suspended",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Deprecated",
        "Deleted",
        "Draft",
        "Errored",
        "Suspended",
    )
)


def serialize_json(value: FlowStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowStatus value: {data!r}")
    return cast(FlowStatus, data)
