"""Generated from Smithy shape ``com.amazonaws.fms#GetNotificationChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_arn


class GetNotificationChannelResponse(TypedDict):
    sns_topic_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The SNS topic that records Firewall Manager activity. </p>"""
    sns_role_name: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The IAM role that is used by Firewall Manager to record activity to SNS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNotificationChannelResponse) -> dict:
    out: dict = {}
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "sns_role_name" in value:
        out["SnsRoleName"] = value["sns_role_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNotificationChannelResponse:
    out: GetNotificationChannelResponse = {}  # type: ignore[typeddict-item]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "SnsRoleName" in data:
        out["sns_role_name"] = data["SnsRoleName"]
    return out
