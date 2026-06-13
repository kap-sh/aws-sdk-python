"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_value

CategoryValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.category_value.CategoryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> CategoryValueList:
    return list(data)
