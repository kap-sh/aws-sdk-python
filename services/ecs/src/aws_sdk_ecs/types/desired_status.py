"""Generated from Smithy shape ``com.amazonaws.ecs#DesiredStatus``."""

from typing import Literal, TypeAlias, cast

DesiredStatus: TypeAlias = Literal[
    "RUNNING",
    "PENDING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DesiredStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DesiredStatus:
    return cast(DesiredStatus, data)
