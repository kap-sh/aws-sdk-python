"""Generated from Smithy shape ``com.amazonaws.fis#ActionParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.action_parameter_description
    import capo_fis.types.action_parameter_required


class ActionParameter(TypedDict, closed=True):
    description: NotRequired[
        "capo_fis.types.action_parameter_description.ActionParameterDescription"
    ]
    """<p>The parameter description.</p>"""
    required: NotRequired[
        "capo_fis.types.action_parameter_required.ActionParameterRequired"
    ]
    """<p>Indicates whether the parameter is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionParameter) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> ActionParameter:
    out: ActionParameter = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "required" in data:
        out["required"] = data["required"]
    return out
