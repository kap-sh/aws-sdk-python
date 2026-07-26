"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_name


class ListMigrationWorkflowTemplatesRequest(TypedDict, closed=True):
    max_results: "capo_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    name: NotRequired["capo_migrationhuborchestrator.types.template_name.TemplateName"]
    """<p>The name of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowTemplatesRequest:
    out: ListMigrationWorkflowTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
