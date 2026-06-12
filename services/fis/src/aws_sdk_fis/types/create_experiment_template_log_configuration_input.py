"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateLogConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input
    import aws_sdk_fis.types.experiment_template_s3_log_configuration_input
    import aws_sdk_fis.types.log_schema_version


class CreateExperimentTemplateLogConfigurationInput(TypedDict):
    cloud_watch_logs_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.ExperimentTemplateCloudWatchLogsLogConfigurationInput"
    ]
    """<p>The configuration for experiment logging to Amazon CloudWatch Logs.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_template_s3_log_configuration_input.ExperimentTemplateS3LogConfigurationInput"
    ]
    """<p>The configuration for experiment logging to Amazon S3.</p>"""
    log_schema_version: "aws_sdk_fis.types.log_schema_version.LogSchemaVersion"
    """<p>The schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateLogConfigurationInput) -> dict:
    out: dict = {}
    if "cloud_watch_logs_configuration" in value:
        import aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input

        out["cloudWatchLogsConfiguration"] = (
            aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.serialize_json(
                value["cloud_watch_logs_configuration"]
            )
        )
    if "s3_configuration" in value:
        import aws_sdk_fis.types.experiment_template_s3_log_configuration_input

        out["s3Configuration"] = (
            aws_sdk_fis.types.experiment_template_s3_log_configuration_input.serialize_json(
                value["s3_configuration"]
            )
        )
    out["logSchemaVersion"] = value["log_schema_version"]
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateLogConfigurationInput:
    out: CreateExperimentTemplateLogConfigurationInput = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogsConfiguration" in data:
        import aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input

        out["cloud_watch_logs_configuration"] = (
            aws_sdk_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.deserialize_json(
                data["cloudWatchLogsConfiguration"]
            )
        )
    if "s3Configuration" in data:
        import aws_sdk_fis.types.experiment_template_s3_log_configuration_input

        out["s3_configuration"] = (
            aws_sdk_fis.types.experiment_template_s3_log_configuration_input.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "logSchemaVersion" in data:
        out["log_schema_version"] = data["logSchemaVersion"]
    else:
        raise DeserializationError(
            "CreateExperimentTemplateLogConfigurationInput.log_schema_version required"
        )
    return out
