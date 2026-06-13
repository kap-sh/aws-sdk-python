"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_filter_value

QuickResponseFilterValueList: TypeAlias = list[
    "aws_sdk_wisdom.types.quick_response_filter_value.QuickResponseFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> QuickResponseFilterValueList:
    return list(data)
