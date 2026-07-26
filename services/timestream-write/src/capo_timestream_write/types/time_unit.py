"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TimeUnit``."""

from typing import Literal, TypeAlias, cast

TimeUnit: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
    "MICROSECONDS",
    "NANOSECONDS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TimeUnit:
    return cast(TimeUnit, data)
