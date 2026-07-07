"""Generated from Smithy shape ``com.amazonaws.emr#MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.cloud_watch_log_configuration
    import aws_sdk_emr.types.s3_logging_configuration


class MonitoringConfiguration(TypedDict, closed=True):
    cloud_watch_log_configuration: NotRequired[
        "aws_sdk_emr.types.cloud_watch_log_configuration.CloudWatchLogConfiguration"
    ]
    """<p>CloudWatch log configuration settings and metadata that specify settings like log files to monitor and where to send them.</p>"""
    s3_logging_configuration: NotRequired[
        "aws_sdk_emr.types.s3_logging_configuration.S3LoggingConfiguration"
    ]
    """<p>S3 logging configuration that controls how different types of logs (system logs, application logs, and persistent UI logs) are uploaded to S3. Each log type can be configured with a specific upload policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_log_configuration" in value:
        import aws_sdk_emr.types.cloud_watch_log_configuration

        out["CloudWatchLogConfiguration"] = (
            aws_sdk_emr.types.cloud_watch_log_configuration.serialize_aws_json_1_1(
                value["cloud_watch_log_configuration"]
            )
        )
    if "s3_logging_configuration" in value:
        import aws_sdk_emr.types.s3_logging_configuration

        out["S3LoggingConfiguration"] = (
            aws_sdk_emr.types.s3_logging_configuration.serialize_aws_json_1_1(
                value["s3_logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogConfiguration" in data:
        import aws_sdk_emr.types.cloud_watch_log_configuration

        out["cloud_watch_log_configuration"] = (
            aws_sdk_emr.types.cloud_watch_log_configuration.deserialize_aws_json_1_1(
                data["CloudWatchLogConfiguration"]
            )
        )
    if "S3LoggingConfiguration" in data:
        import aws_sdk_emr.types.s3_logging_configuration

        out["s3_logging_configuration"] = (
            aws_sdk_emr.types.s3_logging_configuration.deserialize_aws_json_1_1(
                data["S3LoggingConfiguration"]
            )
        )
    return out
