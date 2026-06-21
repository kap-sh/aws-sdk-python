"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterSelectAllOptions``."""

from typing import Literal, TypeAlias, cast

CategoryFilterSelectAllOptions: TypeAlias = Literal["FILTER_ALL_VALUES",]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilterSelectAllOptions) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterSelectAllOptions:
    return cast(CategoryFilterSelectAllOptions, data)
