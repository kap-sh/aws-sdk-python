"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectLogsConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details
    import capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details


class AwsCodeBuildProjectLogsConfigDetails(TypedDict, closed=True):
    cloud_watch_logs: NotRequired[
        "capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails"
    ]
    """<p>Information about CloudWatch Logs for the build project.</p>"""
    s3_logs: NotRequired[
        "capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.AwsCodeBuildProjectLogsConfigS3LogsDetails"
    ]
    """<p>Information about logs built to an S3 bucket for a build project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectLogsConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details

        out["CloudWatchLogs"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "s3_logs" in value:
        import capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details

        out["S3Logs"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.serialize_json(
                value["s3_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectLogsConfigDetails:
    out: AwsCodeBuildProjectLogsConfigDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogs" in data:
        import capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details

        out["cloud_watch_logs"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.deserialize_json(
                data["CloudWatchLogs"]
            )
        )
    if "S3Logs" in data:
        import capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details

        out["s3_logs"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.deserialize_json(
                data["S3Logs"]
            )
        )
    return out
