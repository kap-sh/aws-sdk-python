"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.action_parameters


class ComponentEvent(TypedDict):
    action: NotRequired["str"]
    """<p>The action to perform when a specific event is raised.</p>"""
    parameters: NotRequired[
        "aws_sdk_amplifyuibuilder.types.action_parameters.ActionParameters"
    ]
    """<p>Describes information about the action.</p>"""
    binding_event: NotRequired["str"]
    """<p>Binds an event to an action on a component. When you specify a <code>bindingEvent</code>, the event is called when the action is performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentEvent) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "parameters" in value:
        import aws_sdk_amplifyuibuilder.types.action_parameters

        out["parameters"] = (
            aws_sdk_amplifyuibuilder.types.action_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "binding_event" in value:
        out["bindingEvent"] = value["binding_event"]
    return out


def deserialize_json(data: dict) -> ComponentEvent:
    out: ComponentEvent = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    if "parameters" in data:
        import aws_sdk_amplifyuibuilder.types.action_parameters

        out["parameters"] = (
            aws_sdk_amplifyuibuilder.types.action_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if "bindingEvent" in data:
        out["binding_event"] = data["bindingEvent"]
    return out
