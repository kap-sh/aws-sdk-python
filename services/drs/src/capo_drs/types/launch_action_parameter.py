"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_parameter_type
    import capo_drs.types.launch_action_parameter_value


class LaunchActionParameter(TypedDict, closed=True):
    value: NotRequired[
        "capo_drs.types.launch_action_parameter_value.LaunchActionParameterValue"
    ]
    """<p>Value.</p>"""
    type: NotRequired[
        "capo_drs.types.launch_action_parameter_type.LaunchActionParameterType"
    ]
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
