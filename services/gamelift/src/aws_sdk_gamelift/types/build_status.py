"""Generated from Smithy shape ``com.amazonaws.gamelift#BuildStatus``."""

from typing import Literal, TypeAlias, cast

BuildStatus: TypeAlias = Literal[
    "INITIALIZED",
    "READY",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildStatus:
    return cast(BuildStatus, data)
