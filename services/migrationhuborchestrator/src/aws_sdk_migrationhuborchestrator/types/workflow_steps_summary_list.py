"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_summary

WorkflowStepsSummaryList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.workflow_step_summary.WorkflowStepSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepsSummaryList) -> list:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkflowStepsSummaryList:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_summary

    out: WorkflowStepsSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_summary.deserialize_json(
                item
            )
        )
    return out
