"""Generated from Smithy shape ``com.amazonaws.codepipeline#StartTimeRange``."""

from typing import Literal, TypeAlias, cast

StartTimeRange: TypeAlias = Literal[
    "Latest",
    "All",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTimeRange) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartTimeRange:
    return cast(StartTimeRange, data)
