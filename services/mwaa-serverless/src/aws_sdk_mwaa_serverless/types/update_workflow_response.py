"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UpdateWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.warning_messages
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_version


class UpdateWorkflowResponse(TypedDict, closed=True):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the updated workflow.</p>"""
    modified_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was last modified, in ISO 8601 date-time format.</p>"""
    workflow_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the updated workflow.</p>"""
    warnings: NotRequired[
        "aws_sdk_mwaa_serverless.types.warning_messages.WarningMessages"
    ]
    """<p>Warning messages generated during workflow update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "modified_at" in value:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "warnings" in value:
        import aws_sdk_mwaa_serverless.types.warning_messages

        out["Warnings"] = (
            aws_sdk_mwaa_serverless.types.warning_messages.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkflowResponse:
    out: UpdateWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("UpdateWorkflowResponse.workflow_arn required")
    if "ModifiedAt" in data:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "Warnings" in data:
        import aws_sdk_mwaa_serverless.types.warning_messages

        out["warnings"] = (
            aws_sdk_mwaa_serverless.types.warning_messages.deserialize_aws_json_1_0(
                data["Warnings"]
            )
        )
    return out
