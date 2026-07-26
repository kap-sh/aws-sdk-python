"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_id


class ListTemplateStepGroupsRequest(TypedDict, closed=True):
    max_results: "capo_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplateStepGroupsRequest:
    out: ListTemplateStepGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
