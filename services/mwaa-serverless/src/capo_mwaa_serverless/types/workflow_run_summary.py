"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.run_detail_summary
    import capo_mwaa_serverless.types.run_type
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn


class WorkflowRunSummary(TypedDict, closed=True):
    run_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the workflow run.</p>"""
    workflow_arn: NotRequired["capo_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this run.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow used for this run.</p>"""
    run_type: NotRequired["capo_mwaa_serverless.types.run_type.RunType"]
    """<p>The type of workflow run.</p>"""
    run_detail_summary: NotRequired[
        "capo_mwaa_serverless.types.run_detail_summary.RunDetailSummary"
    ]
    """<p>Summary details about the workflow run execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowRunSummary) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_type" in value:
        import capo_mwaa_serverless.types.run_type

        out["RunType"] = capo_mwaa_serverless.types.run_type.serialize_aws_json_1_0(
            value["run_type"]
        )
    if "run_detail_summary" in value:
        import capo_mwaa_serverless.types.run_detail_summary

        out["RunDetailSummary"] = (
            capo_mwaa_serverless.types.run_detail_summary.serialize_aws_json_1_0(
                value["run_detail_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowRunSummary:
    out: WorkflowRunSummary = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "RunType" in data:
        import capo_mwaa_serverless.types.run_type

        out["run_type"] = capo_mwaa_serverless.types.run_type.deserialize_aws_json_1_0(
            data["RunType"]
        )
    if "RunDetailSummary" in data:
        import capo_mwaa_serverless.types.run_detail_summary

        out["run_detail_summary"] = (
            capo_mwaa_serverless.types.run_detail_summary.deserialize_aws_json_1_0(
                data["RunDetailSummary"]
            )
        )
    return out
