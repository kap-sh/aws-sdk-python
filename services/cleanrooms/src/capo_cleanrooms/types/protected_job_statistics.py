"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.billed_job_resource_utilization


class ProtectedJobStatistics(TypedDict, closed=True):
    total_duration_in_millis: NotRequired["int"]
    """<p>The duration of the protected job, from creation until job completion, in milliseconds.</p>"""
    billed_resource_utilization: NotRequired[
        "capo_cleanrooms.types.billed_job_resource_utilization.BilledJobResourceUtilization"
    ]
    """<p> The billed resource utilization for the protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobStatistics) -> dict:
    out: dict = {}
    if "total_duration_in_millis" in value:
        out["totalDurationInMillis"] = value["total_duration_in_millis"]
    if "billed_resource_utilization" in value:
        import capo_cleanrooms.types.billed_job_resource_utilization

        out["billedResourceUtilization"] = (
            capo_cleanrooms.types.billed_job_resource_utilization.serialize_json(
                value["billed_resource_utilization"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobStatistics:
    out: ProtectedJobStatistics = {}  # type: ignore[typeddict-item]
    if "totalDurationInMillis" in data:
        out["total_duration_in_millis"] = data["totalDurationInMillis"]
    if "billedResourceUtilization" in data:
        import capo_cleanrooms.types.billed_job_resource_utilization

        out["billed_resource_utilization"] = (
            capo_cleanrooms.types.billed_job_resource_utilization.deserialize_json(
                data["billedResourceUtilization"]
            )
        )
    return out
