"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

DeviceStatus: TypeAlias = Literal[
    "REGISTERED",
    "DEREGISTERING",
    "DEREGISTERED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERED",
        "DEREGISTERING",
        "DEREGISTERED",
        "ARCHIVED",
    )
)


def serialize_json(value: DeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceStatus value: {data!r}")
    return cast(DeviceStatus, data)
