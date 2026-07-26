"""Generated from Smithy shape ``com.amazonaws.quicksight#SingleYAxisOption``."""

from typing import Literal, TypeAlias, cast

SingleYAxisOption: TypeAlias = Literal["PRIMARY_Y_AXIS",]


# --- restJson1 ser/de ---
def serialize_json(value: SingleYAxisOption) -> str:
    return value


def deserialize_json(data: str) -> SingleYAxisOption:
    return cast(SingleYAxisOption, data)
