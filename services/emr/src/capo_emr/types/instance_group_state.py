"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupState``."""

from typing import Literal, TypeAlias, cast

InstanceGroupState: TypeAlias = Literal[
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "RECONFIGURING",
    "RESIZING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
    "ARRESTED",
    "SHUTTING_DOWN",
    "ENDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupState:
    return cast(InstanceGroupState, data)
