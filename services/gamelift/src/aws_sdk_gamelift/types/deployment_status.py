"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "IMPAIRED",
    "COMPLETE",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "CANCELLED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "IMPAIRED",
        "COMPLETE",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "CANCELLED",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: DeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
