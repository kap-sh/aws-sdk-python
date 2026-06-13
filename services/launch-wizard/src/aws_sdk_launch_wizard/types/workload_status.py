"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

WorkloadStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "DISABLED",
        "DELETED",
    )
)


def serialize_json(value: WorkloadStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadStatus value: {data!r}")
    return cast(WorkloadStatus, data)
