"""Generated from Smithy shape ``com.amazonaws.emr#SessionMonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.session_cloud_watch_logging_configuration
    import aws_sdk_emr.types.session_managed_logging_configuration
    import aws_sdk_emr.types.session_s3_logging_configuration


class SessionMonitoringConfiguration(TypedDict):
    cloud_watch_logging_configuration: NotRequired[
        "aws_sdk_emr.types.session_cloud_watch_logging_configuration.SessionCloudWatchLoggingConfiguration"
    ]
    """<p>The CloudWatch Logs configuration for the session.</p>"""
    managed_logging_configuration: NotRequired[
        "aws_sdk_emr.types.session_managed_logging_configuration.SessionManagedLoggingConfiguration"
    ]
    """<p>The Amazon EMR-managed logging configuration for the session.</p>"""
    s3_logging_configuration: NotRequired[
        "aws_sdk_emr.types.session_s3_logging_configuration.SessionS3LoggingConfiguration"
    ]
    """<p>The Amazon S3 logging configuration for the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionMonitoringConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_logging_configuration" in value:
        import aws_sdk_emr.types.session_cloud_watch_logging_configuration

        out["CloudWatchLoggingConfiguration"] = (
            aws_sdk_emr.types.session_cloud_watch_logging_configuration.serialize_aws_json_1_1(
                value["cloud_watch_logging_configuration"]
            )
        )
    if "managed_logging_configuration" in value:
        import aws_sdk_emr.types.session_managed_logging_configuration

        out["ManagedLoggingConfiguration"] = (
            aws_sdk_emr.types.session_managed_logging_configuration.serialize_aws_json_1_1(
                value["managed_logging_configuration"]
            )
        )
    if "s3_logging_configuration" in value:
        import aws_sdk_emr.types.session_s3_logging_configuration

        out["S3LoggingConfiguration"] = (
            aws_sdk_emr.types.session_s3_logging_configuration.serialize_aws_json_1_1(
                value["s3_logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionMonitoringConfiguration:
    out: SessionMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "CloudWatchLoggingConfiguration" in data:
        import aws_sdk_emr.types.session_cloud_watch_logging_configuration

        out["cloud_watch_logging_configuration"] = (
            aws_sdk_emr.types.session_cloud_watch_logging_configuration.deserialize_aws_json_1_1(
                data["CloudWatchLoggingConfiguration"]
            )
        )
    if "ManagedLoggingConfiguration" in data:
        import aws_sdk_emr.types.session_managed_logging_configuration

        out["managed_logging_configuration"] = (
            aws_sdk_emr.types.session_managed_logging_configuration.deserialize_aws_json_1_1(
                data["ManagedLoggingConfiguration"]
            )
        )
    if "S3LoggingConfiguration" in data:
        import aws_sdk_emr.types.session_s3_logging_configuration

        out["s3_logging_configuration"] = (
            aws_sdk_emr.types.session_s3_logging_configuration.deserialize_aws_json_1_1(
                data["S3LoggingConfiguration"]
            )
        )
    return out
