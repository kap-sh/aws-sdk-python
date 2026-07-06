"""Generated from Smithy shape ``com.amazonaws.fms#PutNotificationChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_arn


class PutNotificationChannelRequest(TypedDict, closed=True):
    sns_topic_arn: "aws_sdk_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the SNS topic that collects notifications from Firewall Manager.</p>"""
    sns_role_name: "aws_sdk_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record Firewall Manager activity. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutNotificationChannelRequest) -> dict:
    out: dict = {}
    out["SnsTopicArn"] = value["sns_topic_arn"]
    out["SnsRoleName"] = value["sns_role_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutNotificationChannelRequest:
    out: PutNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    else:
        raise DeserializationError(
            "PutNotificationChannelRequest.sns_topic_arn required"
        )
    if "SnsRoleName" in data:
        out["sns_role_name"] = data["SnsRoleName"]
    else:
        raise DeserializationError(
            "PutNotificationChannelRequest.sns_role_name required"
        )
    return out
