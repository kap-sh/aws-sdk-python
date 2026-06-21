"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageRetryMode``."""

from typing import Literal, TypeAlias, cast

StageRetryMode: TypeAlias = Literal[
    "FAILED_ACTIONS",
    "ALL_ACTIONS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageRetryMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageRetryMode:
    return cast(StageRetryMode, data)
