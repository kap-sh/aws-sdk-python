"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#CreateWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.is_latest_version
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.warning_messages
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_status
    import aws_sdk_mwaa_serverless.types.workflow_version


class CreateWorkflowResponse(TypedDict):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the newly created workflow. This ARN uniquely identifies the workflow resource.</p>"""
    created_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was created, in ISO 8601 date-time format.</p>"""
    revision_id: NotRequired["str"]
    """<p>A unique identifier for this revision of the workflow configuration. This ID changes when the workflow is updated and you can use it for optimistic concurrency control in update operations. The revision ID helps prevent conflicting updates and ensures that updates are applied to the expected version of the workflow configuration.</p>"""
    workflow_status: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow. Possible values are <code>READY</code> (workflow is ready to run) and <code>DELETING</code> (workflow is being deleted).</p>"""
    workflow_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the workflow. This is a service-generated alphanumeric string that uniquely identifies this version of the workflow. Amazon Managed Workflows for Apache Airflow Serverless uses a version-first approach where each workflow can have multiple immutable versions, which allows you to maintain different configurations and roll back to previous versions as needed. The version identifier is used in ARNs and API operations to reference specific workflow versions.</p>"""
    is_latest_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.is_latest_version.IsLatestVersion"
    ]
    """<p>A Boolean flag that indicates whether this workflow version is the latest version of the workflow.</p>"""
    warnings: NotRequired[
        "aws_sdk_mwaa_serverless.types.warning_messages.WarningMessages"
    ]
    """<p>Warning messages generated during workflow creation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "created_at" in value:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["CreatedAt"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "workflow_status" in value:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
            )
        )
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "is_latest_version" in value:
        out["IsLatestVersion"] = value["is_latest_version"]
    if "warnings" in value:
        import aws_sdk_mwaa_serverless.types.warning_messages

        out["Warnings"] = (
            aws_sdk_mwaa_serverless.types.warning_messages.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkflowResponse:
    out: CreateWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("CreateWorkflowResponse.workflow_arn required")
    if "CreatedAt" in data:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["created_at"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    if "WorkflowStatus" in data:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
            )
        )
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "IsLatestVersion" in data:
        out["is_latest_version"] = data["IsLatestVersion"]
    if "Warnings" in data:
        import aws_sdk_mwaa_serverless.types.warning_messages

        out["warnings"] = (
            aws_sdk_mwaa_serverless.types.warning_messages.deserialize_aws_json_1_0(
                data["Warnings"]
            )
        )
    return out
