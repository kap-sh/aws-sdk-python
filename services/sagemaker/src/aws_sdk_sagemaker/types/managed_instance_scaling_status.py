"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedInstanceScalingStatus``."""

from typing import Literal, TypeAlias, cast

ManagedInstanceScalingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstanceScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstanceScalingStatus:
    return cast(ManagedInstanceScalingStatus, data)
