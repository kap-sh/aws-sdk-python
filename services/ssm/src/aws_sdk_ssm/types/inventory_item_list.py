"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item

InventoryItemList: TypeAlias = list["aws_sdk_ssm.types.inventory_item.InventoryItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemList) -> list:
    import aws_sdk_ssm.types.inventory_item

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.inventory_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemList:
    import aws_sdk_ssm.types.inventory_item

    out: InventoryItemList = []
    for item in data:
        out.append(aws_sdk_ssm.types.inventory_item.deserialize_aws_json_1_1(item))
    return out
