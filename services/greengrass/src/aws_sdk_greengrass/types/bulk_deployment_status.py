"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The current status of the bulk deployment."""
BulkDeploymentStatus: TypeAlias = Literal[
    "Initializing",
    "Running",
    "Completed",
    "Stopping",
    "Stopped",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "Running",
        "Completed",
        "Stopping",
        "Stopped",
        "Failed",
    )
)


def serialize_json(value: BulkDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> BulkDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BulkDeploymentStatus value: {data!r}")
    return cast(BulkDeploymentStatus, data)
