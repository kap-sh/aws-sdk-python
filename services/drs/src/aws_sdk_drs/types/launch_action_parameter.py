"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionParameter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_parameter_type
    import aws_sdk_drs.types.launch_action_parameter_value

class LaunchActionParameter(TypedDict):
    value: NotRequired["aws_sdk_drs.types.launch_action_parameter_value.LaunchActionParameterValue"]
    """<p>Value.</p>"""
    type: NotRequired["aws_sdk_drs.types.launch_action_parameter_type.LaunchActionParameterType"]
    """<p>Type.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionParameter) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> LaunchActionParameter:
    out: LaunchActionParameter = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "type" in data:
        out["type"] = data["type"]
    return out