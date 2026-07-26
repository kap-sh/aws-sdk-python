"""Generated from Smithy shape ``com.amazonaws.batch#ArrayPropertiesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.array_job_status_summary
    import capo_batch.types.integer
    import capo_batch.types.long


class ArrayPropertiesSummary(TypedDict, closed=True):
    size: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The size of the array job. This parameter is returned for parent array jobs.</p>"""
    index: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The job index within the array that's associated with this job. This parameter is returned for children of array jobs.</p>"""
    status_summary: NotRequired[
        "capo_batch.types.array_job_status_summary.ArrayJobStatusSummary"
    ]
    """<p>A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.</p>"""
    status_summary_last_updated_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the <code>statusSummary</code> was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArrayPropertiesSummary) -> dict:
    out: dict = {}
    if "size" in value:
        out["size"] = value["size"]
    if "index" in value:
        out["index"] = value["index"]
    if "status_summary" in value:
        import capo_batch.types.array_job_status_summary

        out["statusSummary"] = capo_batch.types.array_job_status_summary.serialize_json(
            value["status_summary"]
        )
    if "status_summary_last_updated_at" in value:
        out["statusSummaryLastUpdatedAt"] = value["status_summary_last_updated_at"]
    return out


def deserialize_json(data: dict) -> ArrayPropertiesSummary:
    out: ArrayPropertiesSummary = {}  # type: ignore[typeddict-item]
    if "size" in data:
        out["size"] = data["size"]
    if "index" in data:
        out["index"] = data["index"]
    if "statusSummary" in data:
        import capo_batch.types.array_job_status_summary

        out["status_summary"] = (
            capo_batch.types.array_job_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    if "statusSummaryLastUpdatedAt" in data:
        out["status_summary_last_updated_at"] = data["statusSummaryLastUpdatedAt"]
    return out
