"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PutScalingPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.alarms
    import aws_sdk_application_auto_scaling.types.resource_id_max_len1600


class PutScalingPolicyResponse(TypedDict):
    policy_arn: "aws_sdk_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The Amazon Resource Name (ARN) of the resulting scaling policy.</p>"""
    alarms: NotRequired["aws_sdk_application_auto_scaling.types.alarms.Alarms"]
    """<p>The CloudWatch alarms created for the target tracking scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScalingPolicyResponse) -> dict:
    out: dict = {}
    out["PolicyARN"] = value["policy_arn"]
    if "alarms" in value:
        import aws_sdk_application_auto_scaling.types.alarms

        out["Alarms"] = (
            aws_sdk_application_auto_scaling.types.alarms.serialize_aws_json_1_1(
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
        import aws_sdk_application_auto_scaling.types.alarms

        out["alarms"] = (
            aws_sdk_application_auto_scaling.types.alarms.deserialize_aws_json_1_1(
                data["Alarms"]
            )
        )
    return out
