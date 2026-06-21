"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackState``."""

from typing import Literal, TypeAlias, cast

ConformancePackState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConformancePackState:
    return cast(ConformancePackState, data)
