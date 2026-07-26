"""Generated from Smithy shape ``com.amazonaws.emr#InstanceStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

InstanceStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "BOOTSTRAP_FAILURE",
    "CLUSTER_TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStateChangeReasonCode:
    return cast(InstanceStateChangeReasonCode, data)
