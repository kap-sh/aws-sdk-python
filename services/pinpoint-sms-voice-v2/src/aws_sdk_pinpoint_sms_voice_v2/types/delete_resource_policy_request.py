"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name


class DeleteResourcePolicyRequest(TypedDict):
    resource_arn: (
        "aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource you're deleting the resource-based policy from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    return out
