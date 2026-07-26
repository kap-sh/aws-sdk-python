"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ReplayState``."""

from typing import Literal, TypeAlias, cast

ReplayState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "CANCELLING",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplayState:
    return cast(ReplayState, data)
