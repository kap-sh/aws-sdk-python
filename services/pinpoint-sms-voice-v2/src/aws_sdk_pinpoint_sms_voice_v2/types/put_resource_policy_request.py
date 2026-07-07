"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name
    import aws_sdk_pinpoint_sms_voice_v2.types.resource_policy


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource to attach the resource-based policy to.</p>"""
    policy: "aws_sdk_pinpoint_sms_voice_v2.types.resource_policy.ResourcePolicy"
    """<p>The JSON formatted resource-based policy to attach.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out
