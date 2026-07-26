"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DataFusionRuntimeType``."""

from typing import Literal, TypeAlias, cast

DataFusionRuntimeType: TypeAlias = Literal[
    "multi-thread",
    "multi-thread-alt",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataFusionRuntimeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataFusionRuntimeType:
    return cast(DataFusionRuntimeType, data)
