"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.layer_custom_action_name
    import aws_sdk_quicksight.types.layer_custom_action_operation_list
    import aws_sdk_quicksight.types.layer_custom_action_trigger
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.widget_status


class LayerCustomAction(TypedDict):
    custom_action_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the custom action.</p>"""
    name: "aws_sdk_quicksight.types.layer_custom_action_name.LayerCustomActionName"
    """<p>The name of the custom action.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the <code>LayerCustomAction</code>.</p>"""
    trigger: (
        "aws_sdk_quicksight.types.layer_custom_action_trigger.LayerCustomActionTrigger"
    )
    """<p>The trigger of the <code>LayerCustomAction</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>DATA_POINT_CLICK</code>: Initiates a custom action by a left pointer click on a data point.</p> </li> <li> <p> <code>DATA_POINT_MENU</code>: Initiates a custom action by right pointer click from the menu.</p> </li> </ul>"""
    action_operations: "aws_sdk_quicksight.types.layer_custom_action_operation_list.LayerCustomActionOperationList"
    """<p>A list of <code>LayerCustomActionOperations</code>.</p> <p>This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerCustomAction) -> dict:
    out: dict = {}
    out["CustomActionId"] = value["custom_action_id"]
    out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_quicksight.types.widget_status

        out["Status"] = aws_sdk_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import aws_sdk_quicksight.types.layer_custom_action_trigger

    out["Trigger"] = (
        aws_sdk_quicksight.types.layer_custom_action_trigger.serialize_json(
            value["trigger"]
        )
    )
    import aws_sdk_quicksight.types.layer_custom_action_operation_list

    out["ActionOperations"] = (
        aws_sdk_quicksight.types.layer_custom_action_operation_list.serialize_json(
            value["action_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> LayerCustomAction:
    out: LayerCustomAction = {}  # type: ignore[typeddict-item]
    if "CustomActionId" in data:
        out["custom_action_id"] = data["CustomActionId"]
    else:
        raise DeserializationError("LayerCustomAction.custom_action_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LayerCustomAction.name required")
    if "Status" in data:
        import aws_sdk_quicksight.types.widget_status

        out["status"] = aws_sdk_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if "Trigger" in data:
        import aws_sdk_quicksight.types.layer_custom_action_trigger

        out["trigger"] = (
            aws_sdk_quicksight.types.layer_custom_action_trigger.deserialize_json(
                data["Trigger"]
            )
        )
    else:
        raise DeserializationError("LayerCustomAction.trigger required")
    if "ActionOperations" in data:
        import aws_sdk_quicksight.types.layer_custom_action_operation_list

        out["action_operations"] = (
            aws_sdk_quicksight.types.layer_custom_action_operation_list.deserialize_json(
                data["ActionOperations"]
            )
        )
    else:
        raise DeserializationError("LayerCustomAction.action_operations required")
    return out
