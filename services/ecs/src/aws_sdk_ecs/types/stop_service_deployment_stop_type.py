"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentStopType``."""

from typing import Literal, TypeAlias, cast

StopServiceDeploymentStopType: TypeAlias = Literal[
    "ABORT",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopServiceDeploymentStopType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopServiceDeploymentStopType:
    return cast(StopServiceDeploymentStopType, data)
