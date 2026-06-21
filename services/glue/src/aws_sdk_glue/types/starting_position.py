"""Generated from Smithy shape ``com.amazonaws.glue#StartingPosition``."""

from typing import Literal, TypeAlias, cast

StartingPosition: TypeAlias = Literal[
    "latest",
    "trim_horizon",
    "earliest",
    "timestamp",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartingPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartingPosition:
    return cast(StartingPosition, data)
