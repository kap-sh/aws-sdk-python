"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.workflow_run_summary

WorkflowRunSummaries: TypeAlias = list[
    "capo_mwaa_serverless.types.workflow_run_summary.WorkflowRunSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowRunSummaries) -> list:
    import capo_mwaa_serverless.types.workflow_run_summary

    out: list = []
    for item in value:
        out.append(
            capo_mwaa_serverless.types.workflow_run_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowRunSummaries:
    import capo_mwaa_serverless.types.workflow_run_summary

    out: WorkflowRunSummaries = []
    for item in data:
        out.append(
            capo_mwaa_serverless.types.workflow_run_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
