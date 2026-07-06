"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration
    import aws_sdk_fis.types.experiment_s3_log_configuration
    import aws_sdk_fis.types.log_schema_version


class ExperimentLogConfiguration(TypedDict, closed=True):
    cloud_watch_logs_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration.ExperimentCloudWatchLogsLogConfiguration"
    ]
    """<p>The configuration for experiment logging to Amazon CloudWatch Logs.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_s3_log_configuration.ExperimentS3LogConfiguration"
    ]
    """<p>The configuration for experiment logging to Amazon S3.</p>"""
    log_schema_version: NotRequired[
        "aws_sdk_fis.types.log_schema_version.LogSchemaVersion"
    ]
    """<p>The schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentLogConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_logs_configuration" in value:
        import aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration

        out["cloudWatchLogsConfiguration"] = (
            aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration.serialize_json(
                value["cloud_watch_logs_configuration"]
            )
        )
    if "s3_configuration" in value:
        import aws_sdk_fis.types.experiment_s3_log_configuration

        out["s3Configuration"] = (
            aws_sdk_fis.types.experiment_s3_log_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "log_schema_version" in value:
        out["logSchemaVersion"] = value["log_schema_version"]
    return out


def deserialize_json(data: dict) -> ExperimentLogConfiguration:
    out: ExperimentLogConfiguration = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogsConfiguration" in data:
        import aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration

        out["cloud_watch_logs_configuration"] = (
            aws_sdk_fis.types.experiment_cloud_watch_logs_log_configuration.deserialize_json(
                data["cloudWatchLogsConfiguration"]
            )
        )
    if "s3Configuration" in data:
        import aws_sdk_fis.types.experiment_s3_log_configuration

        out["s3_configuration"] = (
            aws_sdk_fis.types.experiment_s3_log_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "logSchemaVersion" in data:
        out["log_schema_version"] = data["logSchemaVersion"]
    return out
