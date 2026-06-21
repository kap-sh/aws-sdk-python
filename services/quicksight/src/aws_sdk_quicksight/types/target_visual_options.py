"""Generated from Smithy shape ``com.amazonaws.quicksight#TargetVisualOptions``."""

from typing import Literal, TypeAlias, cast

TargetVisualOptions: TypeAlias = Literal["ALL_VISUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: TargetVisualOptions) -> str:
    return value


def deserialize_json(data: str) -> TargetVisualOptions:
    return cast(TargetVisualOptions, data)
