"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateActionInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.action_id
    import capo_fis.types.experiment_template_action_description
    import capo_fis.types.experiment_template_action_parameter_map
    import capo_fis.types.experiment_template_action_start_after_list
    import capo_fis.types.experiment_template_action_target_map


class UpdateExperimentTemplateActionInputItem(TypedDict, closed=True):
    action_id: NotRequired["capo_fis.types.action_id.ActionId"]
    """<p>The ID of the action.</p>"""
    description: NotRequired[
        "capo_fis.types.experiment_template_action_description.ExperimentTemplateActionDescription"
    ]
    """<p>A description for the action.</p>"""
    parameters: NotRequired[
        "capo_fis.types.experiment_template_action_parameter_map.ExperimentTemplateActionParameterMap"
    ]
    """<p>The parameters for the action, if applicable.</p>"""
    targets: NotRequired[
        "capo_fis.types.experiment_template_action_target_map.ExperimentTemplateActionTargetMap"
    ]
    """<p>The targets for the action.</p>"""
    start_after: NotRequired[
        "capo_fis.types.experiment_template_action_start_after_list.ExperimentTemplateActionStartAfterList"
    ]
    """<p>The name of the action that must be completed before the current action starts. Omit this parameter to run the action at the start of the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateActionInputItem) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_fis.types.experiment_template_action_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_template_action_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "targets" in value:
        import capo_fis.types.experiment_template_action_target_map

        out["targets"] = (
            capo_fis.types.experiment_template_action_target_map.serialize_json(
                value["targets"]
            )
        )
    if "start_after" in value:
        import capo_fis.types.experiment_template_action_start_after_list

        out["startAfter"] = (
            capo_fis.types.experiment_template_action_start_after_list.serialize_json(
                value["start_after"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateActionInputItem:
    out: UpdateExperimentTemplateActionInputItem = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import capo_fis.types.experiment_template_action_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_template_action_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if "targets" in data:
        import capo_fis.types.experiment_template_action_target_map

        out["targets"] = (
            capo_fis.types.experiment_template_action_target_map.deserialize_json(
                data["targets"]
            )
        )
    if "startAfter" in data:
        import capo_fis.types.experiment_template_action_start_after_list

        out["start_after"] = (
            capo_fis.types.experiment_template_action_start_after_list.deserialize_json(
                data["startAfter"]
            )
        )
    return out
