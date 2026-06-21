"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#State``."""

from typing import Literal, TypeAlias, cast

State: TypeAlias = Literal[
    "Active",
    "Suppressed",
    "Baseline",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: State) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> State:
    return cast(State, data)
