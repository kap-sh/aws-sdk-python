"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagStatusEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status
    import aws_sdk_cost_explorer.types.tag_key


class CostAllocationTagStatusEntry(TypedDict, closed=True):
    tag_key: "aws_sdk_cost_explorer.types.tag_key.TagKey"
    """<p>The key for the cost allocation tag. </p>"""
    status: (
        "aws_sdk_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
    )
    """<p>The status of a cost allocation tag. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagStatusEntry) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status

    out["Status"] = (
        aws_sdk_cost_explorer.types.cost_allocation_tag_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAllocationTagStatusEntry:
    out: CostAllocationTagStatusEntry = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("CostAllocationTagStatusEntry.tag_key required")
    if "Status" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_status

        out["status"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CostAllocationTagStatusEntry.status required")
    return out
