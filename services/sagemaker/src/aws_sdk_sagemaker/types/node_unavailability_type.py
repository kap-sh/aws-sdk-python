"""Generated from Smithy shape ``com.amazonaws.sagemaker#NodeUnavailabilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NodeUnavailabilityType: TypeAlias = Literal[
    "INSTANCE_COUNT",
    "CAPACITY_PERCENTAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE_COUNT",
        "CAPACITY_PERCENTAGE",
    )
)


def serialize_aws_json_1_1(value: NodeUnavailabilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeUnavailabilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeUnavailabilityType value: {data!r}")
    return cast(NodeUnavailabilityType, data)
