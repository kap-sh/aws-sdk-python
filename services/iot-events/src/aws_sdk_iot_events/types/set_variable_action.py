"""Generated from Smithy shape ``com.amazonaws.iotevents#SetVariableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.variable_name
    import aws_sdk_iot_events.types.variable_value


class SetVariableAction(TypedDict, closed=True):
    variable_name: "aws_sdk_iot_events.types.variable_name.VariableName"
    """<p>The name of the variable.</p>"""
    value: "aws_sdk_iot_events.types.variable_value.VariableValue"
    """<p>The new value of the variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetVariableAction) -> dict:
    out: dict = {}
    out["variableName"] = value["variable_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SetVariableAction:
    out: SetVariableAction = {}  # type: ignore[typeddict-item]
    if "variableName" in data:
        out["variable_name"] = data["variableName"]
    else:
        raise DeserializationError("SetVariableAction.variable_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SetVariableAction.value required")
    return out
