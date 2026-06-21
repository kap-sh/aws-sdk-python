"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyState``."""

from typing import Literal, TypeAlias, cast

AutoScalingPolicyState: TypeAlias = Literal[
    "PENDING",
    "ATTACHING",
    "ATTACHED",
    "DETACHING",
    "DETACHED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingPolicyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoScalingPolicyState:
    return cast(AutoScalingPolicyState, data)
