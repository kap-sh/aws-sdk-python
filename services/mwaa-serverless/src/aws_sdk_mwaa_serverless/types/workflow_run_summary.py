"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.run_detail_summary
    import aws_sdk_mwaa_serverless.types.run_type
    import aws_sdk_mwaa_serverless.types.version_id
    import aws_sdk_mwaa_serverless.types.workflow_arn


class WorkflowRunSummary(TypedDict):
    run_id: NotRequired["aws_sdk_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the workflow run.</p>"""
    workflow_arn: NotRequired["aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this run.</p>"""
    workflow_version: NotRequired["aws_sdk_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow used for this run.</p>"""
    run_type: NotRequired["aws_sdk_mwaa_serverless.types.run_type.RunType"]
    """<p>The type of workflow run.</p>"""
    run_detail_summary: NotRequired[
        "aws_sdk_mwaa_serverless.types.run_detail_summary.RunDetailSummary"
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
        import aws_sdk_mwaa_serverless.types.run_type

        out["RunType"] = aws_sdk_mwaa_serverless.types.run_type.serialize_aws_json_1_0(
            value["run_type"]
        )
    if "run_detail_summary" in value:
        import aws_sdk_mwaa_serverless.types.run_detail_summary

        out["RunDetailSummary"] = (
            aws_sdk_mwaa_serverless.types.run_detail_summary.serialize_aws_json_1_0(
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
        import aws_sdk_mwaa_serverless.types.run_type

        out["run_type"] = (
            aws_sdk_mwaa_serverless.types.run_type.deserialize_aws_json_1_0(
                data["RunType"]
            )
        )
    if "RunDetailSummary" in data:
        import aws_sdk_mwaa_serverless.types.run_detail_summary

        out["run_detail_summary"] = (
            aws_sdk_mwaa_serverless.types.run_detail_summary.deserialize_aws_json_1_0(
                data["RunDetailSummary"]
            )
        )
    return out
