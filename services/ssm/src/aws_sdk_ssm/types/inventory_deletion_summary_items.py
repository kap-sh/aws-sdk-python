"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_deletion_summary_item

InventoryDeletionSummaryItems: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_deletion_summary_item.InventoryDeletionSummaryItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionSummaryItems) -> list:
    import aws_sdk_ssm.types.inventory_deletion_summary_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.inventory_deletion_summary_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryDeletionSummaryItems:
    import aws_sdk_ssm.types.inventory_deletion_summary_item

    out: InventoryDeletionSummaryItems = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_deletion_summary_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
