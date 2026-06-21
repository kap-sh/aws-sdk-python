"""Generated from Smithy shape ``com.amazonaws.devicefarm#InteractionMode``."""

from typing import Literal, TypeAlias, cast

InteractionMode: TypeAlias = Literal[
    "INTERACTIVE",
    "NO_VIDEO",
    "VIDEO_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InteractionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InteractionMode:
    return cast(InteractionMode, data)
