"""Generated from Smithy shape ``com.amazonaws.ecs#SchedulingStrategy``."""

from typing import Literal, TypeAlias, cast

SchedulingStrategy: TypeAlias = Literal[
    "REPLICA",
    "DAEMON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchedulingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulingStrategy:
    return cast(SchedulingStrategy, data)
