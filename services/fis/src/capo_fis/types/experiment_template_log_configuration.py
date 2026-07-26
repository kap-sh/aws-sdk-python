"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration
    import capo_fis.types.experiment_template_s3_log_configuration
    import capo_fis.types.log_schema_version


class ExperimentTemplateLogConfiguration(TypedDict, closed=True):
    cloud_watch_logs_configuration: NotRequired[
        "capo_fis.types.experiment_template_cloud_watch_logs_log_configuration.ExperimentTemplateCloudWatchLogsLogConfiguration"
    ]
    """<p>The configuration for experiment logging to Amazon CloudWatch Logs.</p>"""
    s3_configuration: NotRequired[
        "capo_fis.types.experiment_template_s3_log_configuration.ExperimentTemplateS3LogConfiguration"
    ]
    """<p>The configuration for experiment logging to Amazon S3.</p>"""
    log_schema_version: NotRequired[
        "capo_fis.types.log_schema_version.LogSchemaVersion"
    ]
    """<p>The schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateLogConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_logs_configuration" in value:
        import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration

        out["cloudWatchLogsConfiguration"] = (
            capo_fis.types.experiment_template_cloud_watch_logs_log_configuration.serialize_json(
                value["cloud_watch_logs_configuration"]
            )
        )
    if "s3_configuration" in value:
        import capo_fis.types.experiment_template_s3_log_configuration

        out["s3Configuration"] = (
            capo_fis.types.experiment_template_s3_log_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "log_schema_version" in value:
        out["logSchemaVersion"] = value["log_schema_version"]
    return out


def deserialize_json(data: dict) -> ExperimentTemplateLogConfiguration:
    out: ExperimentTemplateLogConfiguration = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogsConfiguration" in data:
        import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration

        out["cloud_watch_logs_configuration"] = (
            capo_fis.types.experiment_template_cloud_watch_logs_log_configuration.deserialize_json(
                data["cloudWatchLogsConfiguration"]
            )
        )
    if "s3Configuration" in data:
        import capo_fis.types.experiment_template_s3_log_configuration

        out["s3_configuration"] = (
            capo_fis.types.experiment_template_s3_log_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "logSchemaVersion" in data:
        out["log_schema_version"] = data["logSchemaVersion"]
    return out
