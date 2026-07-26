"""Generated from Smithy shape ``com.amazonaws.freetier#ActivityStatus``."""

from typing import Literal, TypeAlias, cast

ActivityStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "EXPIRING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActivityStatus:
    return cast(ActivityStatus, data)
