"""Generated from Smithy shape ``com.amazonaws.connectcases#ParentChildFieldOptionsMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.parent_child_field_options_mapping

ParentChildFieldOptionsMappingList: TypeAlias = list[
    "aws_sdk_connectcases.types.parent_child_field_options_mapping.ParentChildFieldOptionsMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentChildFieldOptionsMappingList) -> list:
    import aws_sdk_connectcases.types.parent_child_field_options_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcases.types.parent_child_field_options_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParentChildFieldOptionsMappingList:
    import aws_sdk_connectcases.types.parent_child_field_options_mapping

    out: ParentChildFieldOptionsMappingList = []
    for item in data:
        out.append(
            aws_sdk_connectcases.types.parent_child_field_options_mapping.deserialize_json(
                item
            )
        )
    return out
