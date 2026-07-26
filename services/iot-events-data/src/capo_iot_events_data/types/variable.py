"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Variable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.variable_name
    import capo_iot_events_data.types.variable_value


class Variable(TypedDict, closed=True):
    name: "capo_iot_events_data.types.variable_name.VariableName"
    """<p>The name of the variable.</p>"""
    value: "capo_iot_events_data.types.variable_value.VariableValue"
    """<p>The current value of the variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Variable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Variable:
    out: Variable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Variable.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Variable.value required")
    return out
