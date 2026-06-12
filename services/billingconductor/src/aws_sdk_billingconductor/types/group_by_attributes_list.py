"""Generated from Smithy shape ``com.amazonaws.billingconductor#GroupByAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.group_by_attribute_name

GroupByAttributesList: TypeAlias = list[
    "aws_sdk_billingconductor.types.group_by_attribute_name.GroupByAttributeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByAttributesList) -> list:
    import aws_sdk_billingconductor.types.group_by_attribute_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.group_by_attribute_name.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GroupByAttributesList:
    import aws_sdk_billingconductor.types.group_by_attribute_name

    out: GroupByAttributesList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.group_by_attribute_name.deserialize_json(
                item
            )
        )
    return out
