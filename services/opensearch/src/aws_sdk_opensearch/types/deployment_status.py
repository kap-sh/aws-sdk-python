"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "PENDING_UPDATE",
    "IN_PROGRESS",
    "COMPLETED",
    "NOT_ELIGIBLE",
    "ELIGIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_UPDATE",
        "IN_PROGRESS",
        "COMPLETED",
        "NOT_ELIGIBLE",
        "ELIGIBLE",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
