"""Generated from Smithy shape ``com.amazonaws.networkmonitor#MonitorState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmonitor.errors import DeserializationError

MonitorState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "INACTIVE",
        "ERROR",
        "DELETING",
    )
)


def serialize_json(value: MonitorState) -> str:
    return value


def deserialize_json(data: str) -> MonitorState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorState value: {data!r}")
    return cast(MonitorState, data)
