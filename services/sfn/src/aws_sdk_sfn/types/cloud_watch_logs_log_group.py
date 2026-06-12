"""Generated from Smithy shape ``com.amazonaws.sfn#CloudWatchLogsLogGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn


class CloudWatchLogsLogGroup(TypedDict):
    log_group_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with <code>:*</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudWatchLogsLogGroup) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudWatchLogsLogGroup:
    out: CloudWatchLogsLogGroup = {}  # type: ignore[typeddict-item]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    return out
