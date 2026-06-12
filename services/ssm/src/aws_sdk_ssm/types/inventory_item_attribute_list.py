"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_attribute

InventoryItemAttributeList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_item_attribute.InventoryItemAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemAttributeList) -> list:
    import aws_sdk_ssm.types.inventory_item_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.inventory_item_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemAttributeList:
    import aws_sdk_ssm.types.inventory_item_attribute

    out: InventoryItemAttributeList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_item_attribute.deserialize_aws_json_1_1(item)
        )
    return out
