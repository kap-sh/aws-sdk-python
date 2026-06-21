"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintRunState``."""

from typing import Literal, TypeAlias, cast

BlueprintRunState: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "ROLLING_BACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintRunState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintRunState:
    return cast(BlueprintRunState, data)
