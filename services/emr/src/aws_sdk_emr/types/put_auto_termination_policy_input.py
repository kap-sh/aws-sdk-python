"""Generated from Smithy shape ``com.amazonaws.emr#PutAutoTerminationPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auto_termination_policy
    import aws_sdk_emr.types.cluster_id


class PutAutoTerminationPolicyInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of the Amazon EMR cluster to which the auto-termination policy will be attached.</p>"""
    auto_termination_policy: NotRequired[
        "aws_sdk_emr.types.auto_termination_policy.AutoTerminationPolicy"
    ]
    """<p>Specifies the auto-termination policy to attach to the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAutoTerminationPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "auto_termination_policy" in value:
        import aws_sdk_emr.types.auto_termination_policy

        out["AutoTerminationPolicy"] = (
            aws_sdk_emr.types.auto_termination_policy.serialize_aws_json_1_1(
                value["auto_termination_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAutoTerminationPolicyInput:
    out: PutAutoTerminationPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "AutoTerminationPolicy" in data:
        import aws_sdk_emr.types.auto_termination_policy

        out["auto_termination_policy"] = (
            aws_sdk_emr.types.auto_termination_policy.deserialize_aws_json_1_1(
                data["AutoTerminationPolicy"]
            )
        )
    return out
