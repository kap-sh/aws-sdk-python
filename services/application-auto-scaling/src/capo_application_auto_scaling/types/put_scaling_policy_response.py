"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PutScalingPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.alarms
    import capo_application_auto_scaling.types.resource_id_max_len1600


class PutScalingPolicyResponse(TypedDict, closed=True):
    policy_arn: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The Amazon Resource Name (ARN) of the resulting scaling policy.</p>"""
    alarms: NotRequired["capo_application_auto_scaling.types.alarms.Alarms"]
    """<p>The CloudWatch alarms created for the target tracking scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScalingPolicyResponse) -> dict:
    out: dict = {}
    out["PolicyARN"] = value["policy_arn"]
    if "alarms" in value:
        import capo_application_auto_scaling.types.alarms

        out["Alarms"] = (
            capo_application_auto_scaling.types.alarms.serialize_aws_json_1_1(
                value["alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutScalingPolicyResponse:
    out: PutScalingPolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyARN" in data:
        out["policy_arn"] = data["PolicyARN"]
    else:
        raise DeserializationError("PutScalingPolicyResponse.policy_arn required")
    if "Alarms" in data:
        import capo_application_auto_scaling.types.alarms

        out["alarms"] = (
            capo_application_auto_scaling.types.alarms.deserialize_aws_json_1_1(
                data["Alarms"]
            )
        )
    return out
