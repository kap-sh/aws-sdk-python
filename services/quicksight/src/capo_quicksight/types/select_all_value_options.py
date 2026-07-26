"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectAllValueOptions``."""

from typing import Literal, TypeAlias, cast

SelectAllValueOptions: TypeAlias = Literal["ALL_VALUES",]


# --- restJson1 ser/de ---
def serialize_json(value: SelectAllValueOptions) -> str:
    return value


def deserialize_json(data: str) -> SelectAllValueOptions:
    return cast(SelectAllValueOptions, data)
