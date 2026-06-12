"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterCapacityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterCapacityType: TypeAlias = Literal[
    "Spot",
    "OnDemand",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Spot",
        "OnDemand",
    )
)


def serialize_aws_json_1_1(value: ClusterCapacityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterCapacityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterCapacityType value: {data!r}")
    return cast(ClusterCapacityType, data)
