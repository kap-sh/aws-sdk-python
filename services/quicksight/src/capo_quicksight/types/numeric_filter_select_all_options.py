"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericFilterSelectAllOptions``."""

from typing import Literal, TypeAlias, cast

NumericFilterSelectAllOptions: TypeAlias = Literal["FILTER_ALL_VALUES",]


# --- restJson1 ser/de ---
def serialize_json(value: NumericFilterSelectAllOptions) -> str:
    return value


def deserialize_json(data: str) -> NumericFilterSelectAllOptions:
    return cast(NumericFilterSelectAllOptions, data)
