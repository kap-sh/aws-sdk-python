"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item

InventoryItemList: TypeAlias = list["capo_ssm.types.inventory_item.InventoryItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemList) -> list:
    import capo_ssm.types.inventory_item

    out: list = []
    for item in value:
        out.append(capo_ssm.types.inventory_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemList:
    import capo_ssm.types.inventory_item

    out: InventoryItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.inventory_item.deserialize_aws_json_1_1(item))
    return out
