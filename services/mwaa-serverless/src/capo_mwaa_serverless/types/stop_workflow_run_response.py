"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#StopWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_run_status


class StopWorkflowRunResponse(TypedDict, closed=True):
    workflow_arn: NotRequired["capo_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the stopped run.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow that was stopped.</p>"""
    run_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the stopped workflow run.</p>"""
    status: NotRequired[
        "capo_mwaa_serverless.types.workflow_run_status.WorkflowRunStatus"
    ]
    """<p>The status of the workflow run after the stop operation. This is typically <code>STOPPING</code> or <code>STOPPED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopWorkflowRunResponse) -> dict:
    out: dict = {}
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import capo_mwaa_serverless.types.workflow_run_status

        out["Status"] = (
            capo_mwaa_serverless.types.workflow_run_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StopWorkflowRunResponse:
    out: StopWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "Status" in data:
        import capo_mwaa_serverless.types.workflow_run_status

        out["status"] = (
            capo_mwaa_serverless.types.workflow_run_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
