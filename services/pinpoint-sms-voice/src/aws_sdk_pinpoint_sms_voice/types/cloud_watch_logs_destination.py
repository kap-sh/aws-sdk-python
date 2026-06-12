"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#CloudWatchLogsDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.string


class CloudWatchLogsDestination(TypedDict):
    iam_role_arn: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination."""
    log_group_arn: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The name of the Amazon CloudWatch Log Group that you want to record events in."""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsDestination) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsDestination:
    out: CloudWatchLogsDestination = {}  # type: ignore[typeddict-item]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
