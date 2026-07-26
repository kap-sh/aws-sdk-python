"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelCountersForWorkteam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.label_counter


class LabelCountersForWorkteam(TypedDict, closed=True):
    human_labeled: NotRequired["capo_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of data objects labeled by a human worker.</p>"""
    pending_human: NotRequired["capo_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of data objects that need to be labeled by a human worker.</p>"""
    total: NotRequired["capo_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of tasks in the labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelCountersForWorkteam) -> dict:
    out: dict = {}
    if "human_labeled" in value:
        out["HumanLabeled"] = value["human_labeled"]
    if "pending_human" in value:
        out["PendingHuman"] = value["pending_human"]
    if "total" in value:
        out["Total"] = value["total"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelCountersForWorkteam:
    out: LabelCountersForWorkteam = {}  # type: ignore[typeddict-item]
    if "HumanLabeled" in data:
        out["human_labeled"] = data["HumanLabeled"]
    if "PendingHuman" in data:
        out["pending_human"] = data["PendingHuman"]
    if "Total" in data:
        out["total"] = data["Total"]
    return out
