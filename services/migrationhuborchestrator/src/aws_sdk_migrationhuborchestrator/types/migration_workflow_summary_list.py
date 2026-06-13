"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#MigrationWorkflowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary

MigrationWorkflowSummaryList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.migration_workflow_summary.MigrationWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationWorkflowSummaryList) -> list:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.migration_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MigrationWorkflowSummaryList:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary

    out: MigrationWorkflowSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.migration_workflow_summary.deserialize_json(
                item
            )
        )
    return out
