"""Generated from Smithy shape ``com.amazonaws.wickr#Setting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class Setting(TypedDict, closed=True):
    option_name: "capo_wickr.types.generic_string.GenericString"
    """<p>The name of the network setting (e.g., 'enableClientMetrics', 'dataRetention').</p>"""
    value: "capo_wickr.types.generic_string.GenericString"
    """<p>The current value of the setting as a string. Boolean values are represented as 'true' or 'false'.</p>"""
    type: "capo_wickr.types.generic_string.GenericString"
    """<p>The data type of the setting value (e.g., 'boolean', 'string', 'number').</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Setting) -> dict:
    out: dict = {}
    out["optionName"] = value["option_name"]
    out["value"] = value["value"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Setting:
    out: Setting = {}  # type: ignore[typeddict-item]
    if "optionName" in data:
        out["option_name"] = data["optionName"]
    else:
        raise DeserializationError("Setting.option_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Setting.value required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Setting.type required")
    return out
