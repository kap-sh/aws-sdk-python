"""Generated from Smithy shape ``com.amazonaws.emr#ClusterStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

ClusterStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "INSTANCE_FLEET_TIMEOUT",
    "BOOTSTRAP_FAILURE",
    "USER_REQUEST",
    "STEP_FAILURE",
    "ALL_STEPS_COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterStateChangeReasonCode:
    return cast(ClusterStateChangeReasonCode, data)
