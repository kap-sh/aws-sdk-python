"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedFieldOptions``."""

from typing import Literal, TypeAlias, cast

SelectedFieldOptions: TypeAlias = Literal["ALL_FIELDS",]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedFieldOptions) -> str:
    return value


def deserialize_json(data: str) -> SelectedFieldOptions:
    return cast(SelectedFieldOptions, data)
