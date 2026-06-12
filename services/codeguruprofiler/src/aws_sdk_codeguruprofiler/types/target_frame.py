"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#TargetFrame``."""

from typing import TypeAlias

TargetFrame: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetFrame) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetFrame:
    return list(data)
