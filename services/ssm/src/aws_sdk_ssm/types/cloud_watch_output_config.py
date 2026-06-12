"""Generated from Smithy shape ``com.amazonaws.ssm#CloudWatchOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.cloud_watch_log_group_name
    import aws_sdk_ssm.types.cloud_watch_output_enabled


class CloudWatchOutputConfig(TypedDict):
    cloud_watch_log_group_name: NotRequired[
        "aws_sdk_ssm.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>The name of the CloudWatch Logs log group where you want to send command output. If you don't specify a group name, Amazon Web Services Systems Manager automatically creates a log group for you. The log group uses the following naming format:</p> <p> <code>aws/ssm/<i>SystemsManagerDocumentName</i> </code> </p>"""
    cloud_watch_output_enabled: (
        "aws_sdk_ssm.types.cloud_watch_output_enabled.CloudWatchOutputEnabled"
    )
    """<p>Enables Systems Manager to send command output to CloudWatch Logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchOutputConfig) -> dict:
    out: dict = {}
    if "cloud_watch_log_group_name" in value:
        out["CloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    out["CloudWatchOutputEnabled"] = value.get("cloud_watch_output_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchOutputConfig:
    out: CloudWatchOutputConfig = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogGroupName" in data:
        out["cloud_watch_log_group_name"] = data["CloudWatchLogGroupName"]
    if "CloudWatchOutputEnabled" in data:
        out["cloud_watch_output_enabled"] = data["CloudWatchOutputEnabled"]
    else:
        out["cloud_watch_output_enabled"] = False
    return out
