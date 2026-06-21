"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#EngineVersion``."""

from typing import Literal, TypeAlias, cast

EngineVersion: TypeAlias = Literal[1,]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngineVersion) -> int:
    return value


def deserialize_aws_json_1_0(data: int) -> EngineVersion:
    return cast(EngineVersion, data)
