"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UpdateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.definition_s3_location
    import aws_sdk_mwaa_serverless.types.description_string
    import aws_sdk_mwaa_serverless.types.engine_version
    import aws_sdk_mwaa_serverless.types.generic_string
    import aws_sdk_mwaa_serverless.types.logging_configuration
    import aws_sdk_mwaa_serverless.types.network_configuration
    import aws_sdk_mwaa_serverless.types.role_arn
    import aws_sdk_mwaa_serverless.types.workflow_arn


class UpdateWorkflowRequest(TypedDict, closed=True):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow you want to update.</p>"""
    definition_s3_location: (
        "aws_sdk_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    )
    """<p>The Amazon S3 location where the updated workflow definition file is stored.</p>"""
    role_arn: "aws_sdk_mwaa_serverless.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.</p>"""
    description: NotRequired[
        "aws_sdk_mwaa_serverless.types.description_string.DescriptionString"
    ]
    """<p>An updated description for the workflow.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Updated logging configuration for the workflow.</p>"""
    engine_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.engine_version.EngineVersion"
    ]
    """<p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_mwaa_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Updated network configuration for the workflow execution environment.</p>"""
    trigger_mode: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkflowRequest) -> dict:
    out: dict = {}
    import aws_sdk_mwaa_serverless.types.definition_s3_location

    out["DefinitionS3Location"] = (
        aws_sdk_mwaa_serverless.types.definition_s3_location.serialize_aws_json_1_0(
            value["definition_s3_location"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "network_configuration" in value:
        import aws_sdk_mwaa_serverless.types.network_configuration

        out["NetworkConfiguration"] = (
            aws_sdk_mwaa_serverless.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkflowRequest:
    out: UpdateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "DefinitionS3Location" in data:
        import aws_sdk_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            aws_sdk_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkflowRequest.definition_s3_location required"
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("UpdateWorkflowRequest.role_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
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
    if "NetworkConfiguration" in data:
        import aws_sdk_mwaa_serverless.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_mwaa_serverless.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if "TriggerMode" in data:
        out["trigger_mode"] = data["TriggerMode"]
    return out
