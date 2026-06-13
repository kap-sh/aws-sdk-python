"""Generated from Smithy shape ``com.amazonaws.emr#RemoveManagedScalingPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id


class RemoveManagedScalingPolicyInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p> Specifies the ID of the cluster from which the managed scaling policy will be removed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveManagedScalingPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveManagedScalingPolicyInput:
    out: RemoveManagedScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    return out
