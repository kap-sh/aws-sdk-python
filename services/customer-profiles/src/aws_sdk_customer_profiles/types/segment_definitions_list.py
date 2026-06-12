"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentDefinitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.segment_definition_item

SegmentDefinitionsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.segment_definition_item.SegmentDefinitionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentDefinitionsList) -> list:
    import aws_sdk_customer_profiles.types.segment_definition_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.segment_definition_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SegmentDefinitionsList:
    import aws_sdk_customer_profiles.types.segment_definition_item

    out: SegmentDefinitionsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.segment_definition_item.deserialize_json(
                item
            )
        )
    return out
