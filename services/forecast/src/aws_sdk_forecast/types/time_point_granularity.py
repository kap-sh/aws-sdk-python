"""Generated from Smithy shape ``com.amazonaws.forecast#TimePointGranularity``."""

from typing import Literal, TypeAlias, cast

TimePointGranularity: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimePointGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimePointGranularity:
    return cast(TimePointGranularity, data)
