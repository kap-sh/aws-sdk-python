"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomContentImageScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

CustomContentImageScalingConfiguration: TypeAlias = Literal[
    "FIT_TO_HEIGHT",
    "FIT_TO_WIDTH",
    "DO_NOT_SCALE",
    "SCALE_TO_VISUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomContentImageScalingConfiguration) -> str:
    return value


def deserialize_json(data: str) -> CustomContentImageScalingConfiguration:
    return cast(CustomContentImageScalingConfiguration, data)
