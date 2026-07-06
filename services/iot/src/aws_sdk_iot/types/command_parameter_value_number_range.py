"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueNumberRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.string_parameter_value


class CommandParameterValueNumberRange(TypedDict, closed=True):
    min: "aws_sdk_iot.types.string_parameter_value.StringParameterValue"
    """<p>The minimum value of a numerical range of a command parameter value.</p>"""
    max: "aws_sdk_iot.types.string_parameter_value.StringParameterValue"
    """<p>The maximum value of a numerical range of a command parameter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueNumberRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> CommandParameterValueNumberRange:
    out: CommandParameterValueNumberRange = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("CommandParameterValueNumberRange.min required")
    if "max" in data:
        out["max"] = data["max"]
    else:
        raise DeserializationError("CommandParameterValueNumberRange.max required")
    return out
