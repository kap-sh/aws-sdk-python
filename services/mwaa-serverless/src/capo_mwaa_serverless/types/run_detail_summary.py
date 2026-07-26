"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#RunDetailSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.workflow_run_status


class RunDetailSummary(TypedDict, closed=True):
    status: NotRequired[
        "capo_mwaa_serverless.types.workflow_run_status.WorkflowRunStatus"
    ]
    """<p>The current status of the workflow run.</p>"""
    created_on: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow run was created, in ISO 8601 date-time format.</p>"""
    started_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow run started execution, in ISO 8601 date-time format.</p>"""
    ended_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow run completed execution, in ISO 8601 date-time format. This value is null if the run is not complete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RunDetailSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_mwaa_serverless.types.workflow_run_status

        out["Status"] = (
            capo_mwaa_serverless.types.workflow_run_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_on" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CreatedOn"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_on"]
            )
        )
    if "started_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["StartedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["started_at"]
            )
        )
    if "ended_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["EndedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["ended_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RunDetailSummary:
    out: RunDetailSummary = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_mwaa_serverless.types.workflow_run_status

        out["status"] = (
            capo_mwaa_serverless.types.workflow_run_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "CreatedOn" in data:
        import capo_mwaa_serverless.types.timestamp_value

        out["created_on"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedOn"]
            )
        )
    if "StartedAt" in data:
        import capo_mwaa_serverless.types.timestamp_value

        out["started_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    if "EndedAt" in data:
        import capo_mwaa_serverless.types.timestamp_value

        out["ended_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["EndedAt"]
            )
        )
    return out
