"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_schema_version
    import aws_sdk_ssm.types.remaining_count
    import aws_sdk_ssm.types.resource_count


class InventoryDeletionSummaryItem(TypedDict, closed=True):
    version: NotRequired[
        "aws_sdk_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    ]
    """<p>The inventory type version.</p>"""
    count: "aws_sdk_ssm.types.resource_count.ResourceCount"
    """<p>A count of the number of deleted items.</p>"""
    remaining_count: "aws_sdk_ssm.types.remaining_count.RemainingCount"
    """<p>The remaining number of items to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionSummaryItem) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    out["Count"] = value.get("count", 0)
    out["RemainingCount"] = value.get("remaining_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryDeletionSummaryItem:
    out: InventoryDeletionSummaryItem = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "RemainingCount" in data:
        out["remaining_count"] = data["RemainingCount"]
    else:
        out["remaining_count"] = 0
    return out
