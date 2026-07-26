"""Generated from Smithy shape ``com.amazonaws.sagemaker#PriorityClass``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_scheduler_priority_class_name
    import capo_sagemaker.types.priority_weight


class PriorityClass(TypedDict, closed=True):
    name: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_priority_class_name.ClusterSchedulerPriorityClassName"
    ]
    """<p>Name of the priority class.</p>"""
    weight: NotRequired["capo_sagemaker.types.priority_weight.PriorityWeight"]
    """<p>Weight of the priority class. The value is within a range from 0 to 100, where 0 is the default.</p> <p>A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityClass) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "weight" in value:
        out["Weight"] = value["weight"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PriorityClass:
    out: PriorityClass = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Weight" in data:
        out["weight"] = data["Weight"]
    return out
