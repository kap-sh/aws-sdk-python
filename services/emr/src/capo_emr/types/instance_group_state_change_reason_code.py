"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

InstanceGroupStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "CLUSTER_TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupStateChangeReasonCode:
    return cast(InstanceGroupStateChangeReasonCode, data)
