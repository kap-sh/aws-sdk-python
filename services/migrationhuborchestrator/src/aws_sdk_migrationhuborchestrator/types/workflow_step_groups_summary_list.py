"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepGroupsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary

WorkflowStepGroupsSummaryList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary.WorkflowStepGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepGroupsSummaryList) -> list:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkflowStepGroupsSummaryList:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary

    out: WorkflowStepGroupsSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary.deserialize_json(
                item
            )
        )
    return out
