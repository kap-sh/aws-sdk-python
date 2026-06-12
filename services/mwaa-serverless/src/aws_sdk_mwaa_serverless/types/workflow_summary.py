"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.description_string
    import aws_sdk_mwaa_serverless.types.generic_string
    import aws_sdk_mwaa_serverless.types.name_string
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_status
    import aws_sdk_mwaa_serverless.types.workflow_version


class WorkflowSummary(TypedDict):
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
    workflow_status: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow.</p>"""
    trigger_mode: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowSummary) -> dict:
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
    if "workflow_status" in value:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowSummary:
    out: WorkflowSummary = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("WorkflowSummary.workflow_arn required")
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
    if "WorkflowStatus" in data:
        import aws_sdk_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            aws_sdk_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
            )
        )
    if "TriggerMode" in data:
        out["trigger_mode"] = data["TriggerMode"]
    return out
