"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupScalingMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_count
    import capo_sagemaker.types.target_count


class InstanceGroupScalingMetadata(TypedDict, closed=True):
    instance_count: NotRequired["capo_sagemaker.types.instance_count.InstanceCount"]
    """<p>The current number of instances in the group.</p>"""
    target_count: NotRequired["capo_sagemaker.types.target_count.TargetCount"]
    """<p>The desired number of instances for the group after scaling.</p>"""
    min_count: NotRequired["capo_sagemaker.types.instance_count.InstanceCount"]
    """<p>Minimum instance count of the instance group.</p>"""
    failure_message: NotRequired["str"]
    """<p>An error message describing why the scaling operation failed, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupScalingMetadata) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "target_count" in value:
        out["TargetCount"] = value["target_count"]
    if "min_count" in value:
        out["MinCount"] = value["min_count"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupScalingMetadata:
    out: InstanceGroupScalingMetadata = {}  # type: ignore[typeddict-item]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "TargetCount" in data:
        out["target_count"] = data["TargetCount"]
    if "MinCount" in data:
        out["min_count"] = data["MinCount"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    return out
