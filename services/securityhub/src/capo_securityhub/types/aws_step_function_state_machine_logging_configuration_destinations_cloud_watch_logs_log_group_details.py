"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails(
    TypedDict, closed=True
):
    log_group_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN (ends with <code>:*</code>) of the CloudWatch Logs log group to which you want your logs emitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails,
) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(
    data: dict,
) -> AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails:
    out: AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails = {}  # type: ignore[typeddict-item]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
