"""Generated from Smithy shape ``com.amazonaws.emr#GetAutoTerminationPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id


class GetAutoTerminationPolicyInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of the Amazon EMR cluster for which the auto-termination policy will be fetched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoTerminationPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoTerminationPolicyInput:
    out: GetAutoTerminationPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    return out
