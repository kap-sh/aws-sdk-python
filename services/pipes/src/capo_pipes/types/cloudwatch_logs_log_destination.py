"""Generated from Smithy shape ``com.amazonaws.pipes#CloudwatchLogsLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.cloudwatch_log_group_arn


class CloudwatchLogsLogDestination(TypedDict, closed=True):
    log_group_arn: NotRequired[
        "capo_pipes.types.cloudwatch_log_group_arn.CloudwatchLogGroupArn"
    ]
    """<p>The Amazon Web Services Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchLogsLogDestination) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudwatchLogsLogDestination:
    out: CloudwatchLogsLogDestination = {}  # type: ignore[typeddict-item]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
