"""Generated from Smithy shape ``com.amazonaws.connectcases#ParentChildFieldOptionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.parent_child_field_option_value

ParentChildFieldOptionValueList: TypeAlias = list[
    "capo_connectcases.types.parent_child_field_option_value.ParentChildFieldOptionValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentChildFieldOptionValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParentChildFieldOptionValueList:
    return list(data)
