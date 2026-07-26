"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.application_configuration_name
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_id


class ListMigrationWorkflowsRequest(TypedDict, closed=True):
    max_results: "capo_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_id: NotRequired[
        "capo_migrationhuborchestrator.types.template_id.TemplateId"
    ]
    """<p>The ID of the template.</p>"""
    ads_application_configuration_name: NotRequired[
        "capo_migrationhuborchestrator.types.application_configuration_name.ApplicationConfigurationName"
    ]
    """<p>The name of the application configured in Application Discovery Service.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowsRequest:
    out: ListMigrationWorkflowsRequest = {}  # type: ignore[typeddict-item]
    return out
