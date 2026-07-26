"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetTemplateStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_automation_configuration
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_id
    import capo_migrationhuborchestrator.types.step_output_list
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.template_id


class GetTemplateStepResponse(TypedDict, closed=True):
    id: NotRequired["capo_migrationhuborchestrator.types.step_id.StepId"]
    """<p>The ID of the step.</p>"""
    step_group_id: NotRequired[
        "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    ]
    """<p>The ID of the step group.</p>"""
    template_id: NotRequired[
        "capo_migrationhuborchestrator.types.template_id.TemplateId"
    ]
    """<p>The ID of the template.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step.</p>"""
    step_action_type: NotRequired[
        "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    creation_time: NotRequired["str"]
    """<p>The time at which the step was created.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    outputs: NotRequired[
        "capo_migrationhuborchestrator.types.step_output_list.StepOutputList"
    ]
    """<p>The outputs of the step.</p>"""
    step_automation_configuration: NotRequired[
        "capo_migrationhuborchestrator.types.step_automation_configuration.StepAutomationConfiguration"
    ]
    """<p>The custom script to run tests on source or target environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateStepResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
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
    if "outputs" in value:
        import capo_migrationhuborchestrator.types.step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.step_output_list.serialize_json(
                value["outputs"]
            )
        )
    if "step_automation_configuration" in value:
        import capo_migrationhuborchestrator.types.step_automation_configuration

        out["stepAutomationConfiguration"] = (
            capo_migrationhuborchestrator.types.step_automation_configuration.serialize_json(
                value["step_automation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemplateStepResponse:
    out: GetTemplateStepResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
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
    if "outputs" in data:
        import capo_migrationhuborchestrator.types.step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.step_output_list.deserialize_json(
                data["outputs"]
            )
        )
    if "stepAutomationConfiguration" in data:
        import capo_migrationhuborchestrator.types.step_automation_configuration

        out["step_automation_configuration"] = (
            capo_migrationhuborchestrator.types.step_automation_configuration.deserialize_json(
                data["stepAutomationConfiguration"]
            )
        )
    return out
