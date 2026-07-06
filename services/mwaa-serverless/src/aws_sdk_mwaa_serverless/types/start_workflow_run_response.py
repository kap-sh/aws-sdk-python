"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#StartWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.timestamp_value
    import aws_sdk_mwaa_serverless.types.workflow_run_status


class StartWorkflowRunResponse(TypedDict, closed=True):
    run_id: NotRequired["aws_sdk_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the newly started workflow run.</p>"""
    status: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_run_status.WorkflowRunStatus"
    ]
    """<p>The initial status of the workflow run. This is typically <code>STARTING</code> when you first create the run.</p>"""
    started_at: NotRequired[
        "aws_sdk_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow run was started, in ISO 8601 date-time format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartWorkflowRunResponse) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import aws_sdk_mwaa_serverless.types.workflow_run_status

        out["Status"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "started_at" in value:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["StartedAt"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["started_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartWorkflowRunResponse:
    out: StartWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "Status" in data:
        import aws_sdk_mwaa_serverless.types.workflow_run_status

        out["status"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "StartedAt" in data:
        import aws_sdk_mwaa_serverless.types.timestamp_value

        out["started_at"] = (
            aws_sdk_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    return out
