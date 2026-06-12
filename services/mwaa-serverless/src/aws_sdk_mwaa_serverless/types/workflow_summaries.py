"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_summary

WorkflowSummaries: TypeAlias = list[
    "aws_sdk_mwaa_serverless.types.workflow_summary.WorkflowSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowSummaries) -> list:
    import aws_sdk_mwaa_serverless.types.workflow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mwaa_serverless.types.workflow_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowSummaries:
    import aws_sdk_mwaa_serverless.types.workflow_summary

    out: WorkflowSummaries = []
    for item in data:
        out.append(
            aws_sdk_mwaa_serverless.types.workflow_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
