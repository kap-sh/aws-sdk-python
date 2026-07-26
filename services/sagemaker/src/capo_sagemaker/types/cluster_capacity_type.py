"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterCapacityType``."""

from typing import Literal, TypeAlias, cast

ClusterCapacityType: TypeAlias = Literal[
    "Spot",
    "OnDemand",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterCapacityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterCapacityType:
    return cast(ClusterCapacityType, data)
