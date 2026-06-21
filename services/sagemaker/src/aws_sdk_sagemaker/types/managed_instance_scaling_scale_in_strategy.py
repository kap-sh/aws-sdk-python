"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedInstanceScalingScaleInStrategy``."""

from typing import Literal, TypeAlias, cast

ManagedInstanceScalingScaleInStrategy: TypeAlias = Literal[
    "IDLE_RELEASE",
    "CONSOLIDATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstanceScalingScaleInStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstanceScalingScaleInStrategy:
    return cast(ManagedInstanceScalingScaleInStrategy, data)
