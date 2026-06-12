"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateSchedule``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

SoftwareSetUpdateSchedule: TypeAlias = Literal[
    "USE_MAINTENANCE_WINDOW",
    "APPLY_IMMEDIATELY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE_MAINTENANCE_WINDOW",
        "APPLY_IMMEDIATELY",
    )
)


def serialize_json(value: SoftwareSetUpdateSchedule) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateSchedule:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareSetUpdateSchedule value: {data!r}")
    return cast(SoftwareSetUpdateSchedule, data)
