"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_version_summary

WorkflowVersionSummaries: TypeAlias = list[
    "aws_sdk_mwaa_serverless.types.workflow_version_summary.WorkflowVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowVersionSummaries) -> list:
    import aws_sdk_mwaa_serverless.types.workflow_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mwaa_serverless.types.workflow_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowVersionSummaries:
    import aws_sdk_mwaa_serverless.types.workflow_version_summary

    out: WorkflowVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_mwaa_serverless.types.workflow_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
