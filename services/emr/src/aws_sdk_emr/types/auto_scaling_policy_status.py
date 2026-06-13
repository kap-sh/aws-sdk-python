"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auto_scaling_policy_state
    import aws_sdk_emr.types.auto_scaling_policy_state_change_reason


class AutoScalingPolicyStatus(TypedDict):
    state: NotRequired[
        "aws_sdk_emr.types.auto_scaling_policy_state.AutoScalingPolicyState"
    ]
    """<p>Indicates the status of the automatic scaling policy.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.auto_scaling_policy_state_change_reason.AutoScalingPolicyStateChangeReason"
    ]
    """<p>The reason for a change in status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingPolicyStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.auto_scaling_policy_state

        out["State"] = (
            aws_sdk_emr.types.auto_scaling_policy_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.auto_scaling_policy_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.auto_scaling_policy_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoScalingPolicyStatus:
    out: AutoScalingPolicyStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.auto_scaling_policy_state

        out["state"] = (
            aws_sdk_emr.types.auto_scaling_policy_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.auto_scaling_policy_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.auto_scaling_policy_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    return out
