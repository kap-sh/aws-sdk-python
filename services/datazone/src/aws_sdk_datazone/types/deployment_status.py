"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "PENDING_DEPLOYMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
        "PENDING_DEPLOYMENT",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
