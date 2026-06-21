"""Generated from Smithy shape ``com.amazonaws.inspector#StopAction``."""

from typing import Literal, TypeAlias, cast

StopAction: TypeAlias = Literal[
    "START_EVALUATION",
    "SKIP_EVALUATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopAction:
    return cast(StopAction, data)
