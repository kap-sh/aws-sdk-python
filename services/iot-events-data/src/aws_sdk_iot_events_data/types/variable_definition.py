"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#VariableDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.variable_name
    import aws_sdk_iot_events_data.types.variable_value


class VariableDefinition(TypedDict, closed=True):
    name: "aws_sdk_iot_events_data.types.variable_name.VariableName"
    """<p>The name of the variable.</p>"""
    value: "aws_sdk_iot_events_data.types.variable_value.VariableValue"
    """<p>The new value of the variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariableDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> VariableDefinition:
    out: VariableDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("VariableDefinition.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("VariableDefinition.value required")
    return out
