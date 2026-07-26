"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetTemplateStepGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.template_id


class GetTemplateStepGroupRequest(TypedDict, closed=True):
    template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""
    id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateStepGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTemplateStepGroupRequest:
    out: GetTemplateStepGroupRequest = {}  # type: ignore[typeddict-item]
    return out
