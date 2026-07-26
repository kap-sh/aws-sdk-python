"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagBackfillRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_backfill_status
    import capo_cost_explorer.types.zoned_date_time


class CostAllocationTagBackfillRequest(TypedDict, closed=True):
    backfill_from: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p> The date the backfill starts from. </p>"""
    requested_at: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p> The time when the backfill was requested. </p>"""
    completed_at: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p> The backfill completion time. </p>"""
    backfill_status: NotRequired[
        "capo_cost_explorer.types.cost_allocation_tag_backfill_status.CostAllocationTagBackfillStatus"
    ]
    """<p> The status of the cost allocation tag backfill request. </p>"""
    last_updated_at: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p> The time when the backfill status was last updated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagBackfillRequest) -> dict:
    out: dict = {}
    if "backfill_from" in value:
        out["BackfillFrom"] = value["backfill_from"]
    if "requested_at" in value:
        out["RequestedAt"] = value["requested_at"]
    if "completed_at" in value:
        out["CompletedAt"] = value["completed_at"]
    if "backfill_status" in value:
        import capo_cost_explorer.types.cost_allocation_tag_backfill_status

        out["BackfillStatus"] = (
            capo_cost_explorer.types.cost_allocation_tag_backfill_status.serialize_aws_json_1_1(
                value["backfill_status"]
            )
        )
    if "last_updated_at" in value:
        out["LastUpdatedAt"] = value["last_updated_at"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAllocationTagBackfillRequest:
    out: CostAllocationTagBackfillRequest = {}  # type: ignore[typeddict-item]
    if "BackfillFrom" in data:
        out["backfill_from"] = data["BackfillFrom"]
    if "RequestedAt" in data:
        out["requested_at"] = data["RequestedAt"]
    if "CompletedAt" in data:
        out["completed_at"] = data["CompletedAt"]
    if "BackfillStatus" in data:
        import capo_cost_explorer.types.cost_allocation_tag_backfill_status

        out["backfill_status"] = (
            capo_cost_explorer.types.cost_allocation_tag_backfill_status.deserialize_aws_json_1_1(
                data["BackfillStatus"]
            )
        )
    if "LastUpdatedAt" in data:
        out["last_updated_at"] = data["LastUpdatedAt"]
    return out
