"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.object_map
    import aws_sdk_mwaa_serverless.types.run_type
    import aws_sdk_mwaa_serverless.types.version_id
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_run_detail


class GetWorkflowRunResponse(TypedDict, closed=True):
    workflow_arn: NotRequired["aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this run.</p>"""
    workflow_version: NotRequired["aws_sdk_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow that is used for this run.</p>"""
    run_id: NotRequired["aws_sdk_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of this workflow run.</p>"""
    run_type: NotRequired["aws_sdk_mwaa_serverless.types.run_type.RunType"]
    """<p>The type of workflow run. Values are <code>ON_DEMAND</code> (manually triggered) or <code>SCHEDULED</code> (automatically triggered by schedule).</p>"""
    override_parameters: NotRequired[
        "aws_sdk_mwaa_serverless.types.object_map.ObjectMap"
    ]
    """<p>Parameters that were overridden for this specific workflow run.</p>"""
    run_detail: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_run_detail.WorkflowRunDetail"
    ]
    """<p>Detailed information about the workflow run execution, including timing, status, and task instances.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowRunResponse) -> dict:
    out: dict = {}
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "run_type" in value:
        import aws_sdk_mwaa_serverless.types.run_type

        out["RunType"] = aws_sdk_mwaa_serverless.types.run_type.serialize_aws_json_1_0(
            value["run_type"]
        )
    if "override_parameters" in value:
        import aws_sdk_mwaa_serverless.types.object_map

        out["OverrideParameters"] = (
            aws_sdk_mwaa_serverless.types.object_map.serialize_aws_json_1_0(
                value["override_parameters"]
            )
        )
    if "run_detail" in value:
        import aws_sdk_mwaa_serverless.types.workflow_run_detail

        out["RunDetail"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_detail.serialize_aws_json_1_0(
                value["run_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowRunResponse:
    out: GetWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "RunType" in data:
        import aws_sdk_mwaa_serverless.types.run_type

        out["run_type"] = (
            aws_sdk_mwaa_serverless.types.run_type.deserialize_aws_json_1_0(
                data["RunType"]
            )
        )
    if "OverrideParameters" in data:
        import aws_sdk_mwaa_serverless.types.object_map

        out["override_parameters"] = (
            aws_sdk_mwaa_serverless.types.object_map.deserialize_aws_json_1_0(
                data["OverrideParameters"]
            )
        )
    if "RunDetail" in data:
        import aws_sdk_mwaa_serverless.types.workflow_run_detail

        out["run_detail"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_detail.deserialize_aws_json_1_0(
                data["RunDetail"]
            )
        )
    return out
