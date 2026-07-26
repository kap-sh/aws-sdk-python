"""Generated from Smithy shape ``com.amazonaws.connectcases#ParentChildFieldOptionsMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.parent_child_field_options_mapping

ParentChildFieldOptionsMappingList: TypeAlias = list[
    "capo_connectcases.types.parent_child_field_options_mapping.ParentChildFieldOptionsMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentChildFieldOptionsMappingList) -> list:
    import capo_connectcases.types.parent_child_field_options_mapping

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.parent_child_field_options_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParentChildFieldOptionsMappingList:
    import capo_connectcases.types.parent_child_field_options_mapping

    out: ParentChildFieldOptionsMappingList = []
    for item in data:
        out.append(
            capo_connectcases.types.parent_child_field_options_mapping.deserialize_json(
                item
            )
        )
    return out
