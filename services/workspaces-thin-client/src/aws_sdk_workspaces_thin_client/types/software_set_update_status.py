"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

SoftwareSetUpdateStatus: TypeAlias = Literal[
    "AVAILABLE",
    "IN_PROGRESS",
    "UP_TO_DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "IN_PROGRESS",
        "UP_TO_DATE",
    )
)


def serialize_json(value: SoftwareSetUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareSetUpdateStatus value: {data!r}")
    return cast(SoftwareSetUpdateStatus, data)
