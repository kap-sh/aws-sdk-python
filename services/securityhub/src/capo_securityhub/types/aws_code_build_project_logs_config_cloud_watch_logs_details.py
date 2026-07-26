"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails(TypedDict, closed=True):
    group_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The group name of the logs in CloudWatch Logs.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of the logs in CloudWatch Logs for a build project.</p>"""
    stream_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The prefix of the stream name of the CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails:
    out: AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    return out
