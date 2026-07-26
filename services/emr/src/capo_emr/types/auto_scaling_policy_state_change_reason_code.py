"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

AutoScalingPolicyStateChangeReasonCode: TypeAlias = Literal[
    "USER_REQUEST",
    "PROVISION_FAILURE",
    "CLEANUP_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingPolicyStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoScalingPolicyStateChangeReasonCode:
    return cast(AutoScalingPolicyStateChangeReasonCode, data)
