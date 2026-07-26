"""Generated from Smithy shape ``com.amazonaws.sfn#BillingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.billed_duration
    import capo_sfn.types.billed_memory_used


class BillingDetails(TypedDict, closed=True):
    billed_memory_used_in_mb: "capo_sfn.types.billed_memory_used.BilledMemoryUsed"
    """<p>Billed memory consumption of your workflow, in MB.</p>"""
    billed_duration_in_milliseconds: "capo_sfn.types.billed_duration.BilledDuration"
    """<p>Billed duration of your workflow, in milliseconds.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingDetails) -> dict:
    out: dict = {}
    out["billedMemoryUsedInMB"] = value.get("billed_memory_used_in_mb", 0)
    out["billedDurationInMilliseconds"] = value.get(
        "billed_duration_in_milliseconds", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingDetails:
    out: BillingDetails = {}  # type: ignore[typeddict-item]
    if "billedMemoryUsedInMB" in data:
        out["billed_memory_used_in_mb"] = data["billedMemoryUsedInMB"]
    else:
        out["billed_memory_used_in_mb"] = 0
    if "billedDurationInMilliseconds" in data:
        out["billed_duration_in_milliseconds"] = data["billedDurationInMilliseconds"]
    else:
        out["billed_duration_in_milliseconds"] = 0
    return out
