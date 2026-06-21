"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPolicyUpdateBehavior``."""

from typing import Literal, TypeAlias, cast

ScalingPolicyUpdateBehavior: TypeAlias = Literal[
    "KeepExternalPolicies",
    "ReplaceExternalPolicies",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicyUpdateBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingPolicyUpdateBehavior:
    return cast(ScalingPolicyUpdateBehavior, data)
