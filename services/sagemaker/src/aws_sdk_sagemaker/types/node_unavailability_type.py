"""Generated from Smithy shape ``com.amazonaws.sagemaker#NodeUnavailabilityType``."""

from typing import Literal, TypeAlias, cast

NodeUnavailabilityType: TypeAlias = Literal[
    "INSTANCE_COUNT",
    "CAPACITY_PERCENTAGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeUnavailabilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeUnavailabilityType:
    return cast(NodeUnavailabilityType, data)
