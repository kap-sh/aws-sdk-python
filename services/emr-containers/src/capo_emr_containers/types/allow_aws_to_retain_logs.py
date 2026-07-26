"""Generated from Smithy shape ``com.amazonaws.emrcontainers#AllowAWSToRetainLogs``."""

from typing import Literal, TypeAlias, cast

AllowAWSToRetainLogs: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowAWSToRetainLogs) -> str:
    return value


def deserialize_json(data: str) -> AllowAWSToRetainLogs:
    return cast(AllowAWSToRetainLogs, data)
