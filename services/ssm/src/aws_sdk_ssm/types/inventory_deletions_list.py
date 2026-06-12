"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_deletion_status_item

InventoryDeletionsList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_deletion_status_item.InventoryDeletionStatusItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionsList) -> list:
    import aws_sdk_ssm.types.inventory_deletion_status_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.inventory_deletion_status_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryDeletionsList:
    import aws_sdk_ssm.types.inventory_deletion_status_item

    out: InventoryDeletionsList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_deletion_status_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
