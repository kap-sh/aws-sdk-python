"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.workflow_summary

WorkflowSummaries: TypeAlias = list[
    "aws_sdk_codecatalyst.types.workflow_summary.WorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSummaries) -> list:
    import aws_sdk_codecatalyst.types.workflow_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_codecatalyst.types.workflow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowSummaries:
    import aws_sdk_codecatalyst.types.workflow_summary

    out: WorkflowSummaries = []
    for item in data:
        out.append(aws_sdk_codecatalyst.types.workflow_summary.deserialize_json(item))
    return out
