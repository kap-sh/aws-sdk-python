"""Generated from Smithy shape ``com.amazonaws.emr#PutAutoTerminationPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.auto_termination_policy
    import capo_emr.types.cluster_id


class PutAutoTerminationPolicyInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of the Amazon EMR cluster to which the auto-termination policy will be attached.</p>"""
    auto_termination_policy: NotRequired[
        "capo_emr.types.auto_termination_policy.AutoTerminationPolicy"
    ]
    """<p>Specifies the auto-termination policy to attach to the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAutoTerminationPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "auto_termination_policy" in value:
        import capo_emr.types.auto_termination_policy

        out["AutoTerminationPolicy"] = (
            capo_emr.types.auto_termination_policy.serialize_aws_json_1_1(
                value["auto_termination_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAutoTerminationPolicyInput:
    out: PutAutoTerminationPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "AutoTerminationPolicy" in data:
        import capo_emr.types.auto_termination_policy

        out["auto_termination_policy"] = (
            capo_emr.types.auto_termination_policy.deserialize_aws_json_1_1(
                data["AutoTerminationPolicy"]
            )
        )
    return out
