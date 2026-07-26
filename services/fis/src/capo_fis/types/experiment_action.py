"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.action_id
    import capo_fis.types.experiment_action_description
    import capo_fis.types.experiment_action_end_time
    import capo_fis.types.experiment_action_parameter_map
    import capo_fis.types.experiment_action_start_after_list
    import capo_fis.types.experiment_action_start_time
    import capo_fis.types.experiment_action_state
    import capo_fis.types.experiment_action_target_map


class ExperimentAction(TypedDict, closed=True):
    action_id: NotRequired["capo_fis.types.action_id.ActionId"]
    """<p>The ID of the action.</p>"""
    description: NotRequired[
        "capo_fis.types.experiment_action_description.ExperimentActionDescription"
    ]
    """<p>The description for the action.</p>"""
    parameters: NotRequired[
        "capo_fis.types.experiment_action_parameter_map.ExperimentActionParameterMap"
    ]
    """<p>The parameters for the action.</p>"""
    targets: NotRequired[
        "capo_fis.types.experiment_action_target_map.ExperimentActionTargetMap"
    ]
    """<p>The targets for the action.</p>"""
    start_after: NotRequired[
        "capo_fis.types.experiment_action_start_after_list.ExperimentActionStartAfterList"
    ]
    """<p>The name of the action that must be completed before this action starts.</p>"""
    state: NotRequired["capo_fis.types.experiment_action_state.ExperimentActionState"]
    """<p>The state of the action.</p>"""
    start_time: NotRequired[
        "capo_fis.types.experiment_action_start_time.ExperimentActionStartTime"
    ]
    """<p>The time that the action started.</p>"""
    end_time: NotRequired[
        "capo_fis.types.experiment_action_end_time.ExperimentActionEndTime"
    ]
    """<p>The time that the action ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentAction) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_fis.types.experiment_action_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_action_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "targets" in value:
        import capo_fis.types.experiment_action_target_map

        out["targets"] = capo_fis.types.experiment_action_target_map.serialize_json(
            value["targets"]
        )
    if "start_after" in value:
        import capo_fis.types.experiment_action_start_after_list

        out["startAfter"] = (
            capo_fis.types.experiment_action_start_after_list.serialize_json(
                value["start_after"]
            )
        )
    if "state" in value:
        import capo_fis.types.experiment_action_state

        out["state"] = capo_fis.types.experiment_action_state.serialize_json(
            value["state"]
        )
    if "start_time" in value:
        import capo_fis.types.experiment_action_start_time

        out["startTime"] = capo_fis.types.experiment_action_start_time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_fis.types.experiment_action_end_time

        out["endTime"] = capo_fis.types.experiment_action_end_time.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentAction:
    out: ExperimentAction = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import capo_fis.types.experiment_action_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_action_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if "targets" in data:
        import capo_fis.types.experiment_action_target_map

        out["targets"] = capo_fis.types.experiment_action_target_map.deserialize_json(
            data["targets"]
        )
    if "startAfter" in data:
        import capo_fis.types.experiment_action_start_after_list

        out["start_after"] = (
            capo_fis.types.experiment_action_start_after_list.deserialize_json(
                data["startAfter"]
            )
        )
    if "state" in data:
        import capo_fis.types.experiment_action_state

        out["state"] = capo_fis.types.experiment_action_state.deserialize_json(
            data["state"]
        )
    if "startTime" in data:
        import capo_fis.types.experiment_action_start_time

        out["start_time"] = (
            capo_fis.types.experiment_action_start_time.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_fis.types.experiment_action_end_time

        out["end_time"] = capo_fis.types.experiment_action_end_time.deserialize_json(
            data["endTime"]
        )
    return out
