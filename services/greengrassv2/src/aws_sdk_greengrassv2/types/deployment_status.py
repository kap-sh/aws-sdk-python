"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "ACTIVE",
    "COMPLETED",
    "CANCELED",
    "FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "COMPLETED",
        "CANCELED",
        "FAILED",
        "INACTIVE",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
