"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.definition_s3_location
    import aws_sdk_mwaa_serverless.types.description_string
    import aws_sdk_mwaa_serverless.types.encryption_configuration
    import aws_sdk_mwaa_serverless.types.engine_version
    import aws_sdk_mwaa_serverless.types.generic_string
    import aws_sdk_mwaa_serverless.types.logging_configuration
    import aws_sdk_mwaa_serverless.types.name_string
    import aws_sdk_mwaa_serverless.types.network_configuration
    import aws_sdk_mwaa_serverless.types.role_arn
    import aws_sdk_mwaa_serverless.types.schedule_configuration
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_status
    import aws_sdk_mwaa_serverless.types.workflow_version


class GetWorkflowResponse(TypedDict, closed=True):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow.</p>"""
    workflow_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the workflow.</p>"""
    name: NotRequired["aws_sdk_mwaa_serverless.types.name_string.NameString"]
    """<p>The name of the workflow.</p>"""
    description: NotRequired[
        "aws_sdk_mwaa_serverless.types.description_string.DescriptionString"
    ]
    """<p>The description of the workflow.</p>"""
    created_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was created, in ISO 8601 date-time format.</p>"""
    modified_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was last modified, in ISO 8601 date-time format.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the workflow.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration for the workflow.</p>"""
    engine_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.engine_version.EngineVersion"
    ]
    """<p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that this workflow uses.</p>"""
    workflow_status: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow.</p>"""
    definition_s3_location: NotRequired[
        "aws_sdk_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    ]
    """<p>The Amazon S3 location of the workflow definition file.</p>"""
    schedule_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for the workflow, including cron expressions for automated execution. Amazon Managed Workflows for Apache Airflow Serverless uses EventBridge Scheduler for cost-effective, timezone-aware scheduling. When a workflow includes schedule information in its YAML definition, the service automatically configures the appropriate triggers for automated execution. Only one version of a workflow can have an active schedule at any given time.</p>"""
    role_arn: NotRequired["aws_sdk_mwaa_serverless.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used for workflow execution.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the workflow execution environment.</p>"""
    trigger_mode: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The trigger mode for the workflow execution.</p>"""
    workflow_definition: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The workflow definition content.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "encryption_configuration" in value:
        import aws_sdk_mwaa_serverless.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_mwaa_serverless.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "logging_configuration" in value:
        import aws_sdk_mwaa_serverless.types.logging_configuration

        out["LoggingConfiguration"] = (
            aws_sdk_mwaa_serverless.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "engine_version" in value:
        import aws_sdk_mwaa_serverless.types.engine_version

        out["EngineVersion"] = (
            aws_sdk_mwaa_serverless.types.engine_version.serialize_aws_json_1_0(
                value["engine_version"]
            )
        )
    if "workflow_status" in value:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
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
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "network_configuration" in value:
        import aws_sdk_mwaa_serverless.types.network_configuration

        out["NetworkConfiguration"] = (
            aws_sdk_mwaa_serverless.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    if "workflow_definition" in value:
        out["WorkflowDefinition"] = value["workflow_definition"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("GetWorkflowResponse.workflow_arn required")
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
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
    if "EncryptionConfiguration" in data:
        import aws_sdk_mwaa_serverless.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_mwaa_serverless.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if "LoggingConfiguration" in data:
        import aws_sdk_mwaa_serverless.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_mwaa_serverless.types.logging_configuration.deserialize_aws_json_1_0(
                data["LoggingConfiguration"]
            )
        )
    if "EngineVersion" in data:
        import aws_sdk_mwaa_serverless.types.engine_version

        out["engine_version"] = (
            aws_sdk_mwaa_serverless.types.engine_version.deserialize_aws_json_1_0(
                data["EngineVersion"]
            )
        )
    if "WorkflowStatus" in data:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
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
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "NetworkConfiguration" in data:
        import aws_sdk_mwaa_serverless.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_mwaa_serverless.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if "TriggerMode" in data:
        out["trigger_mode"] = data["TriggerMode"]
    if "WorkflowDefinition" in data:
        out["workflow_definition"] = data["WorkflowDefinition"]
    return out
