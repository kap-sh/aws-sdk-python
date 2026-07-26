"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseQueryFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_query_field

QuickResponseQueryFieldList: TypeAlias = list[
    "capo_wisdom.types.quick_response_query_field.QuickResponseQueryField"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseQueryFieldList) -> list:
    import capo_wisdom.types.quick_response_query_field

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.quick_response_query_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickResponseQueryFieldList:
    import capo_wisdom.types.quick_response_query_field

    out: QuickResponseQueryFieldList = []
    for item in data:
        out.append(capo_wisdom.types.quick_response_query_field.deserialize_json(item))
    return out
