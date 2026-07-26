"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseFilterFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_filter_field

QuickResponseFilterFieldList: TypeAlias = list[
    "capo_wisdom.types.quick_response_filter_field.QuickResponseFilterField"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseFilterFieldList) -> list:
    import capo_wisdom.types.quick_response_filter_field

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.quick_response_filter_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickResponseFilterFieldList:
    import capo_wisdom.types.quick_response_filter_field

    out: QuickResponseFilterFieldList = []
    for item in data:
        out.append(capo_wisdom.types.quick_response_filter_field.deserialize_json(item))
    return out
