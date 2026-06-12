"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectLogsConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details
    import aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details


class AwsCodeBuildProjectLogsConfigDetails(TypedDict):
    cloud_watch_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails"
    ]
    """<p>Information about CloudWatch Logs for the build project.</p>"""
    s3_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.AwsCodeBuildProjectLogsConfigS3LogsDetails"
    ]
    """<p>Information about logs built to an S3 bucket for a build project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectLogsConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details

        out["CloudWatchLogs"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "s3_logs" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details

        out["S3Logs"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.serialize_json(
                value["s3_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectLogsConfigDetails:
    out: AwsCodeBuildProjectLogsConfigDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogs" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details

        out["cloud_watch_logs"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_cloud_watch_logs_details.deserialize_json(
                data["CloudWatchLogs"]
            )
        )
    if "S3Logs" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details

        out["s3_logs"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_s3_logs_details.deserialize_json(
                data["S3Logs"]
            )
        )
    return out
