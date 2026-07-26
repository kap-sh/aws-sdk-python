"""Generated from Smithy shape ``com.amazonaws.machinelearning#RealtimeEndpointStatus``."""

from typing import Literal, TypeAlias, cast

RealtimeEndpointStatus: TypeAlias = Literal[
    "NONE",
    "READY",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RealtimeEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RealtimeEndpointStatus:
    return cast(RealtimeEndpointStatus, data)
