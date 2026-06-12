"""Generated from Smithy shape ``com.amazonaws.iotevents#State``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.on_enter_lifecycle
    import aws_sdk_iot_events.types.on_exit_lifecycle
    import aws_sdk_iot_events.types.on_input_lifecycle
    import aws_sdk_iot_events.types.state_name


class State(TypedDict):
    state_name: "aws_sdk_iot_events.types.state_name.StateName"
    """<p>The name of the state.</p>"""
    on_input: NotRequired[
        "aws_sdk_iot_events.types.on_input_lifecycle.OnInputLifecycle"
    ]
    """<p>When an input is received and the <code>condition</code> is TRUE, perform the specified <code>actions</code>.</p>"""
    on_enter: NotRequired[
        "aws_sdk_iot_events.types.on_enter_lifecycle.OnEnterLifecycle"
    ]
    """<p>When entering this state, perform these <code>actions</code> if the <code>condition</code> is TRUE.</p>"""
    on_exit: NotRequired["aws_sdk_iot_events.types.on_exit_lifecycle.OnExitLifecycle"]
    """<p>When exiting this state, perform these <code>actions</code> if the specified <code>condition</code> is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: State) -> dict:
    out: dict = {}
    out["stateName"] = value["state_name"]
    if "on_input" in value:
        import aws_sdk_iot_events.types.on_input_lifecycle

        out["onInput"] = aws_sdk_iot_events.types.on_input_lifecycle.serialize_json(
            value["on_input"]
        )
    if "on_enter" in value:
        import aws_sdk_iot_events.types.on_enter_lifecycle

        out["onEnter"] = aws_sdk_iot_events.types.on_enter_lifecycle.serialize_json(
            value["on_enter"]
        )
    if "on_exit" in value:
        import aws_sdk_iot_events.types.on_exit_lifecycle

        out["onExit"] = aws_sdk_iot_events.types.on_exit_lifecycle.serialize_json(
            value["on_exit"]
        )
    return out


def deserialize_json(data: dict) -> State:
    out: State = {}  # type: ignore[typeddict-item]
    if "stateName" in data:
        out["state_name"] = data["stateName"]
    else:
        raise DeserializationError("State.state_name required")
    if "onInput" in data:
        import aws_sdk_iot_events.types.on_input_lifecycle

        out["on_input"] = aws_sdk_iot_events.types.on_input_lifecycle.deserialize_json(
            data["onInput"]
        )
    if "onEnter" in data:
        import aws_sdk_iot_events.types.on_enter_lifecycle

        out["on_enter"] = aws_sdk_iot_events.types.on_enter_lifecycle.deserialize_json(
            data["onEnter"]
        )
    if "onExit" in data:
        import aws_sdk_iot_events.types.on_exit_lifecycle

        out["on_exit"] = aws_sdk_iot_events.types.on_exit_lifecycle.deserialize_json(
            data["onExit"]
        )
    return out
