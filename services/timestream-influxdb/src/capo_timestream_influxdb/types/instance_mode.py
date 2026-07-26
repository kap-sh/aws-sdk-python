"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InstanceMode``."""

from typing import Literal, TypeAlias, cast

InstanceMode: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
    "REPLICA",
    "INGEST",
    "QUERY",
    "COMPACT",
    "PROCESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceMode:
    return cast(InstanceMode, data)
