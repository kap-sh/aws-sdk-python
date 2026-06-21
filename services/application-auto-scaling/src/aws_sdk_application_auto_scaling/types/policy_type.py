"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PolicyType``."""

from typing import Literal, TypeAlias, cast

PolicyType: TypeAlias = Literal[
    "StepScaling",
    "TargetTrackingScaling",
    "PredictiveScaling",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyType:
    return cast(PolicyType, data)
