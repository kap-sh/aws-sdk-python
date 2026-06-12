"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.definition_s3_location
    import aws_sdk_mwaa_serverless.types.generic_string
    import aws_sdk_mwaa_serverless.types.is_latest_version
    import aws_sdk_mwaa_serverless.types.schedule_configuration
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_version


class WorkflowVersionSummary(TypedDict):
    workflow_version: "aws_sdk_mwaa_serverless.types.workflow_version.WorkflowVersion"
    """<p>The version identifier of the workflow version.</p>"""
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this version.</p>"""
    is_latest_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.is_latest_version.IsLatestVersion"
    ]
    """<p>Boolean flag that indicates whether this is the latest version of the workflow.</p>"""
    created_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow version was created, in ISO 8601 date-time format.</p>"""
    modified_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow version was last modified, in ISO 8601 date-time format.</p>"""
    definition_s3_location: NotRequired[
        "aws_sdk_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    ]
    """<p>The Amazon S3 location of the workflow definition file for this version.</p>"""
    schedule_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for this workflow version.</p>"""
    trigger_mode: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowVersionSummary) -> dict:
    out: dict = {}
    out["WorkflowVersion"] = value["workflow_version"]
    out["WorkflowArn"] = value["workflow_arn"]
    if "is_latest_version" in value:
        out["IsLatestVersion"] = value["is_latest_version"]
    if "created_at" in value:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["CreatedAt"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "definition_s3_location" in value:
        import aws_sdk_mwaa_serverless.types.definition_s3_location

        out["DefinitionS3Location"] = (
            aws_sdk_mwaa_serverless.types.definition_s3_location.serialize_aws_json_1_0(
                value["definition_s3_location"]
            )
        )
    if "schedule_configuration" in value:
        import aws_sdk_mwaa_serverless.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            aws_sdk_mwaa_serverless.types.schedule_configuration.serialize_aws_json_1_0(
                value["schedule_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowVersionSummary:
    out: WorkflowVersionSummary = {}  # type: ignore[typeddict-item]
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    else:
        raise DeserializationError("WorkflowVersionSummary.workflow_version required")
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("WorkflowVersionSummary.workflow_arn required")
    if "IsLatestVersion" in data:
        out["is_latest_version"] = data["IsLatestVersion"]
    if "CreatedAt" in data:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["created_at"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "ModifiedAt" in data:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if "DefinitionS3Location" in data:
        import aws_sdk_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            aws_sdk_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    if "ScheduleConfiguration" in data:
        import aws_sdk_mwaa_serverless.types.schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_mwaa_serverless.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    if "TriggerMode" in data:
        out["trigger_mode"] = data["TriggerMode"]
    return out
