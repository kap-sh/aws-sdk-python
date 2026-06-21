"""Generated from Smithy shape ``com.amazonaws.glue#ResourceState``."""

from typing import Literal, TypeAlias, cast

ResourceState: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCESS",
    "STOPPED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceState:
    return cast(ResourceState, data)
