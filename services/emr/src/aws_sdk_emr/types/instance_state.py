"""Generated from Smithy shape ``com.amazonaws.emr#InstanceState``."""

from typing import Literal, TypeAlias, cast

InstanceState: TypeAlias = Literal[
    "AWAITING_FULFILLMENT",
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceState:
    return cast(InstanceState, data)
