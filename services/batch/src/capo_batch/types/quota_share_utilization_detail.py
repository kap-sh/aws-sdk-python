"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareUtilizationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.quota_share_capacity_utilization_list


class QuotaShareUtilizationDetail(TypedDict, closed=True):
    top_capacity_utilization: NotRequired[
        "capo_batch.types.quota_share_capacity_utilization_list.QuotaShareCapacityUtilizationList"
    ]
    """<p>A list of the top capacity utilizations across quota shares associated with a job queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareUtilizationDetail) -> dict:
    out: dict = {}
    if "top_capacity_utilization" in value:
        import capo_batch.types.quota_share_capacity_utilization_list

        out["topCapacityUtilization"] = (
            capo_batch.types.quota_share_capacity_utilization_list.serialize_json(
                value["top_capacity_utilization"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuotaShareUtilizationDetail:
    out: QuotaShareUtilizationDetail = {}  # type: ignore[typeddict-item]
    if "topCapacityUtilization" in data:
        import capo_batch.types.quota_share_capacity_utilization_list

        out["top_capacity_utilization"] = (
            capo_batch.types.quota_share_capacity_utilization_list.deserialize_json(
                data["topCapacityUtilization"]
            )
        )
    return out
