"""Generated from Smithy shape ``com.amazonaws.pipes#CloudwatchLogsLogDestinationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.cloudwatch_log_group_arn


class CloudwatchLogsLogDestinationParameters(TypedDict, closed=True):
    log_group_arn: "aws_sdk_pipes.types.cloudwatch_log_group_arn.CloudwatchLogGroupArn"
    """<p>The Amazon Web Services Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchLogsLogDestinationParameters) -> dict:
    out: dict = {}
    out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudwatchLogsLogDestinationParameters:
    out: CloudwatchLogsLogDestinationParameters = {}  # type: ignore[typeddict-item]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    else:
        raise DeserializationError(
            "CloudwatchLogsLogDestinationParameters.log_group_arn required"
        )
    return out
