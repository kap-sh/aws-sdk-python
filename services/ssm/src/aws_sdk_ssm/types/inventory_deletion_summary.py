"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_deletion_summary_items
    import aws_sdk_ssm.types.remaining_count
    import aws_sdk_ssm.types.total_count


class InventoryDeletionSummary(TypedDict):
    total_count: "aws_sdk_ssm.types.total_count.TotalCount"
    """<p>The total number of items to delete. This count doesn't change during the delete operation.</p>"""
    remaining_count: "aws_sdk_ssm.types.remaining_count.RemainingCount"
    """<p>Remaining number of items to delete.</p>"""
    summary_items: NotRequired[
        "aws_sdk_ssm.types.inventory_deletion_summary_items.InventoryDeletionSummaryItems"
    ]
    """<p>A list of counts and versions for deleted items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionSummary) -> dict:
    out: dict = {}
    out["TotalCount"] = value.get("total_count", 0)
    out["RemainingCount"] = value.get("remaining_count", 0)
    if "summary_items" in value:
        import aws_sdk_ssm.types.inventory_deletion_summary_items

        out["SummaryItems"] = (
            aws_sdk_ssm.types.inventory_deletion_summary_items.serialize_aws_json_1_1(
                value["summary_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryDeletionSummary:
    out: InventoryDeletionSummary = {}  # type: ignore[typeddict-item]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    else:
        out["total_count"] = 0
    if "RemainingCount" in data:
        out["remaining_count"] = data["RemainingCount"]
    else:
        out["remaining_count"] = 0
    if "SummaryItems" in data:
        import aws_sdk_ssm.types.inventory_deletion_summary_items

        out["summary_items"] = (
            aws_sdk_ssm.types.inventory_deletion_summary_items.deserialize_aws_json_1_1(
                data["SummaryItems"]
            )
        )
    return out
