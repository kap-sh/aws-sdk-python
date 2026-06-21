"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklineAxisBehavior``."""

from typing import Literal, TypeAlias, cast

SparklineAxisBehavior: TypeAlias = Literal[
    "SHARED",
    "INDEPENDENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SparklineAxisBehavior) -> str:
    return value


def deserialize_json(data: str) -> SparklineAxisBehavior:
    return cast(SparklineAxisBehavior, data)
