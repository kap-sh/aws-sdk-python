"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list
    import aws_sdk_migrationhuborchestrator.types.next_token


class ListMigrationWorkflowsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    migration_workflow_summary: "aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list.MigrationWorkflowSummaryList"
    """<p>The summary of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list

    out["migrationWorkflowSummary"] = (
        aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list.serialize_json(
            value["migration_workflow_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowsResponse:
    out: ListMigrationWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "migrationWorkflowSummary" in data:
        import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list

        out["migration_workflow_summary"] = (
            aws_sdk_migrationhuborchestrator.types.migration_workflow_summary_list.deserialize_json(
                data["migrationWorkflowSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListMigrationWorkflowsResponse.migration_workflow_summary required"
        )
    return out
