"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_search_criteria

PredefinedAttributeSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.predefined_attribute_search_criteria.PredefinedAttributeSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSearchConditionList) -> list:
    import aws_sdk_connect.types.predefined_attribute_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.predefined_attribute_search_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PredefinedAttributeSearchConditionList:
    import aws_sdk_connect.types.predefined_attribute_search_criteria

    out: PredefinedAttributeSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.predefined_attribute_search_criteria.deserialize_json(
                item
            )
        )
    return out
