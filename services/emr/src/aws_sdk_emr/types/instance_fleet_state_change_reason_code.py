"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

InstanceFleetStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "CLUSTER_TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetStateChangeReasonCode:
    return cast(InstanceFleetStateChangeReasonCode, data)
