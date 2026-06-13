"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

MonitorStatus: TypeAlias = Literal[
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


def serialize_json(value: MonitorStatus) -> str:
    return value


def deserialize_json(data: str) -> MonitorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorStatus value: {data!r}")
    return cast(MonitorStatus, data)
