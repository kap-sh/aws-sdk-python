"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ActionStatus``."""

from typing import Literal, TypeAlias, cast

ActionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CLIENT_ERROR",
    "FAILED",
    "COMPLETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    return cast(ActionStatus, data)
