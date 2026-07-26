"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.template_id


class ListTemplateStepsRequest(TypedDict, closed=True):
    max_results: "capo_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""
    step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplateStepsRequest:
    out: ListTemplateStepsRequest = {}  # type: ignore[typeddict-item]
    return out
