"""Generated from Smithy shape ``com.amazonaws.sagemaker#Direction``."""

from typing import Literal, TypeAlias, cast

Direction: TypeAlias = Literal[
    "Both",
    "Ascendants",
    "Descendants",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Direction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Direction:
    return cast(Direction, data)
