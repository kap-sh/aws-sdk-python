"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#TargetDeviceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

TargetDeviceStatus: TypeAlias = Literal[
    "DEREGISTERED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEREGISTERED",
        "ARCHIVED",
    )
)


def serialize_json(value: TargetDeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetDeviceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetDeviceStatus value: {data!r}")
    return cast(TargetDeviceStatus, data)
