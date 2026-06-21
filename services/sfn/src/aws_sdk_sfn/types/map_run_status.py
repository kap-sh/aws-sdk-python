"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunStatus``."""

from typing import Literal, TypeAlias, cast

MapRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "ABORTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MapRunStatus:
    return cast(MapRunStatus, data)
