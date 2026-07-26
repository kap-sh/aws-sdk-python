"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateStepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.owner
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.target_type


class TemplateStepSummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    template_id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    step_action_type: NotRequired[
        "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    target_type: NotRequired[
        "capo_migrationhuborchestrator.types.target_type.TargetType"
    ]
    """<p>The servers on which to run the script.</p>"""
    owner: NotRequired["capo_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStepSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "target_type" in value:
        out["targetType"] = value["target_type"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> TemplateStepSummary:
    out: TemplateStepSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "name" in data:
        out["name"] = data["name"]
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
    if "targetType" in data:
        out["target_type"] = data["targetType"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "previous" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    return out
