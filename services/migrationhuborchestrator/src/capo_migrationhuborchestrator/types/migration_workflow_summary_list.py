"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#MigrationWorkflowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_summary

MigrationWorkflowSummaryList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.migration_workflow_summary.MigrationWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationWorkflowSummaryList) -> list:
    import capo_migrationhuborchestrator.types.migration_workflow_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhuborchestrator.types.migration_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MigrationWorkflowSummaryList:
    import capo_migrationhuborchestrator.types.migration_workflow_summary

    out: MigrationWorkflowSummaryList = []
    for item in data:
        out.append(
            capo_migrationhuborchestrator.types.migration_workflow_summary.deserialize_json(
                item
            )
        )
    return out
