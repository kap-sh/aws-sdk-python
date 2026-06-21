"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckState``."""

from typing import Literal, TypeAlias, cast

InstanceHealthCheckState: TypeAlias = Literal[
    "OK",
    "IMPAIRED",
    "INSUFFICIENT_DATA",
    "INITIALIZING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthCheckState:
    return cast(InstanceHealthCheckState, data)
