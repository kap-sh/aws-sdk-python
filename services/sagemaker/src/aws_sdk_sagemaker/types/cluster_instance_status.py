"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterInstanceStatus: TypeAlias = Literal[
    "Running",
    "Failure",
    "Pending",
    "ShuttingDown",
    "SystemUpdating",
    "DeepHealthCheckInProgress",
    "NotFound",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Failure",
        "Pending",
        "ShuttingDown",
        "SystemUpdating",
        "DeepHealthCheckInProgress",
        "NotFound",
    )
)


def serialize_aws_json_1_1(value: ClusterInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterInstanceStatus value: {data!r}")
    return cast(ClusterInstanceStatus, data)
