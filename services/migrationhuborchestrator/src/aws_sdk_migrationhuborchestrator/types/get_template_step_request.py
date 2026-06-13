"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetTemplateStepRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_id
    import aws_sdk_migrationhuborchestrator.types.template_id


class GetTemplateStepRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId"
    """<p>The ID of the step.</p>"""
    template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""
    step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateStepRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTemplateStepRequest:
    out: GetTemplateStepRequest = {}  # type: ignore[typeddict-item]
    return out
