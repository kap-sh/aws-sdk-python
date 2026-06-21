"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlanStatusCode``."""

from typing import Literal, TypeAlias, cast

ScalingPlanStatusCode: TypeAlias = Literal[
    "Active",
    "ActiveWithProblems",
    "CreationInProgress",
    "CreationFailed",
    "DeletionInProgress",
    "DeletionFailed",
    "UpdateInProgress",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlanStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingPlanStatusCode:
    return cast(ScalingPlanStatusCode, data)
