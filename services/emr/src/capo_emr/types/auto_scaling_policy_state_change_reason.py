"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.auto_scaling_policy_state_change_reason_code
    import capo_emr.types.string


class AutoScalingPolicyStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_emr.types.auto_scaling_policy_state_change_reason_code.AutoScalingPolicyStateChangeReasonCode"
    ]
    """<p>The code indicating the reason for the change in status.<code>USER_REQUEST</code> indicates that the scaling policy status was changed by a user. <code>PROVISION_FAILURE</code> indicates that the status change was because the policy failed to provision. <code>CLEANUP_FAILURE</code> indicates an error.</p>"""
    message: NotRequired["capo_emr.types.string.String"]
    """<p>A friendly, more verbose message that accompanies an automatic scaling policy state change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingPolicyStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_emr.types.auto_scaling_policy_state_change_reason_code

        out["Code"] = (
            capo_emr.types.auto_scaling_policy_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoScalingPolicyStateChangeReason:
    out: AutoScalingPolicyStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_emr.types.auto_scaling_policy_state_change_reason_code

        out["code"] = (
            capo_emr.types.auto_scaling_policy_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
