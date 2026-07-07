"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateCloudWatchLogsLogConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.cloud_watch_log_group_arn


class ExperimentTemplateCloudWatchLogsLogConfigurationInput(TypedDict, closed=True):
    log_group_arn: "aws_sdk_fis.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    """<p>The Amazon Resource Name (ARN) of the destination Amazon CloudWatch Logs log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ExperimentTemplateCloudWatchLogsLogConfigurationInput,
) -> dict:
    out: dict = {}
    out["logGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(
    data: dict,
) -> ExperimentTemplateCloudWatchLogsLogConfigurationInput:
    out: ExperimentTemplateCloudWatchLogsLogConfigurationInput = {}  # type: ignore[typeddict-item]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        raise DeserializationError(
            "ExperimentTemplateCloudWatchLogsLogConfigurationInput.log_group_arn required"
        )
    return out
