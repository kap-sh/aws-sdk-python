"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingStatusType``."""

from typing import Literal, TypeAlias, cast

ScalingStatusType: TypeAlias = Literal[
    "ACTIVE",
    "UPDATE_REQUESTED",
    "UPDATING",
    "DELETE_REQUESTED",
    "DELETING",
    "DELETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStatusType:
    return cast(ScalingStatusType, data)
