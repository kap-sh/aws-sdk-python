"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#EngineType``."""

from typing import Literal, TypeAlias, cast

EngineType: TypeAlias = Literal[
    "INFLUXDB_V2",
    "INFLUXDB_V3_CORE",
    "INFLUXDB_V3_ENTERPRISE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngineType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngineType:
    return cast(EngineType, data)
