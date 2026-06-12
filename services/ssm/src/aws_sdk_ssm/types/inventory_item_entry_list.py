"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_entry

InventoryItemEntryList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_item_entry.InventoryItemEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemEntryList) -> list:
    import aws_sdk_ssm.types.inventory_item_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.inventory_item_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemEntryList:
    import aws_sdk_ssm.types.inventory_item_entry

    out: InventoryItemEntryList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_item_entry.deserialize_aws_json_1_1(item)
        )
    return out
