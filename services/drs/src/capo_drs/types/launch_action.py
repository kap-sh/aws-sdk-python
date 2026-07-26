"""Generated from Smithy shape ``com.amazonaws.drs#LaunchAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_category
    import capo_drs.types.launch_action_description
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_name
    import capo_drs.types.launch_action_order
    import capo_drs.types.launch_action_parameters
    import capo_drs.types.launch_action_type
    import capo_drs.types.launch_action_version
    import capo_drs.types.ssm_document_name


class LaunchAction(TypedDict, closed=True):
    action_id: NotRequired["capo_drs.types.launch_action_id.LaunchActionId"]
    action_code: NotRequired["capo_drs.types.ssm_document_name.SsmDocumentName"]
    """<p>Launch action code.</p>"""
    type: NotRequired["capo_drs.types.launch_action_type.LaunchActionType"]
    """<p>Launch action type.</p>"""
    name: NotRequired["capo_drs.types.launch_action_name.LaunchActionName"]
    active: NotRequired["bool"]
    """<p>Whether the launch action is active.</p>"""
    order: NotRequired["capo_drs.types.launch_action_order.LaunchActionOrder"]
    action_version: NotRequired[
        "capo_drs.types.launch_action_version.LaunchActionVersion"
    ]
    optional: NotRequired["bool"]
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    parameters: NotRequired[
        "capo_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: NotRequired[
        "capo_drs.types.launch_action_description.LaunchActionDescription"
    ]
    category: NotRequired["capo_drs.types.launch_action_category.LaunchActionCategory"]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchAction) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "action_code" in value:
        out["actionCode"] = value["action_code"]
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "active" in value:
        out["active"] = value["active"]
    if "order" in value:
        out["order"] = value["order"]
    if "action_version" in value:
        out["actionVersion"] = value["action_version"]
    if "optional" in value:
        out["optional"] = value["optional"]
    if "parameters" in value:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> LaunchAction:
    out: LaunchAction = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "actionCode" in data:
        out["action_code"] = data["actionCode"]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "active" in data:
        out["active"] = data["active"]
    if "order" in data:
        out["order"] = data["order"]
    if "actionVersion" in data:
        out["action_version"] = data["actionVersion"]
    if "optional" in data:
        out["optional"] = data["optional"]
    if "parameters" in data:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "category" in data:
        out["category"] = data["category"]
    return out
