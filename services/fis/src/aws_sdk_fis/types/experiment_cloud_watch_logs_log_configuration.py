"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentCloudWatchLogsLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.cloud_watch_log_group_arn


class ExperimentCloudWatchLogsLogConfiguration(TypedDict, closed=True):
    log_group_arn: NotRequired[
        "aws_sdk_fis.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination Amazon CloudWatch Logs log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentCloudWatchLogsLogConfiguration) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> ExperimentCloudWatchLogsLogConfiguration:
    out: ExperimentCloudWatchLogsLogConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    return out
