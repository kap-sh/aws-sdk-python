"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetState``."""

from typing import Literal, TypeAlias, cast

InstanceFleetState: TypeAlias = Literal[
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "RESIZING",
    "RECONFIGURING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetState:
    return cast(InstanceFleetState, data)
