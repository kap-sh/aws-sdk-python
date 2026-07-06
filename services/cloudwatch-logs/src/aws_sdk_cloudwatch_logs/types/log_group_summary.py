"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.log_group_class
    import aws_sdk_cloudwatch_logs.types.log_group_name


class LogGroupSummary(TypedDict, closed=True):
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    log_group_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the log group.</p>"""
    log_group_class: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    r"""<p>The log group class for this log group. For details about the features supported by each log group class, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html\">Log classes</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupSummary) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    if "log_group_class" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogGroupSummary:
    out: LogGroupSummary = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    if "logGroupClass" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    return out
