"""Generated from Smithy shape ``com.amazonaws.batch#FairshareUtilizationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.fairshare_capacity_utilization_list
    import capo_batch.types.long


class FairshareUtilizationDetail(TypedDict, closed=True):
    active_share_count: NotRequired["capo_batch.types.long.Long"]
    """<p>The total number of active shares in the fairshare scheduling job queue that are currently utilizing capacity.</p>"""
    top_capacity_utilization: NotRequired[
        "capo_batch.types.fairshare_capacity_utilization_list.FairshareCapacityUtilizationList"
    ]
    """<p>A list of the top 20 shares with the highest capacity utilization, ordered by usage amount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FairshareUtilizationDetail) -> dict:
    out: dict = {}
    if "active_share_count" in value:
        out["activeShareCount"] = value["active_share_count"]
    if "top_capacity_utilization" in value:
        import capo_batch.types.fairshare_capacity_utilization_list

        out["topCapacityUtilization"] = (
            capo_batch.types.fairshare_capacity_utilization_list.serialize_json(
                value["top_capacity_utilization"]
            )
        )
    return out


def deserialize_json(data: dict) -> FairshareUtilizationDetail:
    out: FairshareUtilizationDetail = {}  # type: ignore[typeddict-item]
    if "activeShareCount" in data:
        out["active_share_count"] = data["activeShareCount"]
    if "topCapacityUtilization" in data:
        import capo_batch.types.fairshare_capacity_utilization_list

        out["top_capacity_utilization"] = (
            capo_batch.types.fairshare_capacity_utilization_list.deserialize_json(
                data["topCapacityUtilization"]
            )
        )
    return out
