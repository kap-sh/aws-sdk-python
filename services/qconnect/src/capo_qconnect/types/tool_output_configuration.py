"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string


class ToolOutputConfiguration(TypedDict, closed=True):
    output_variable_name_override: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Override the tool output results to different variable name.</p>"""
    session_data_namespace: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The session data namespace for tool output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOutputConfiguration) -> dict:
    out: dict = {}
    if "output_variable_name_override" in value:
        out["outputVariableNameOverride"] = value["output_variable_name_override"]
    if "session_data_namespace" in value:
        out["sessionDataNamespace"] = value["session_data_namespace"]
    return out


def deserialize_json(data: dict) -> ToolOutputConfiguration:
    out: ToolOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "outputVariableNameOverride" in data:
        out["output_variable_name_override"] = data["outputVariableNameOverride"]
    if "sessionDataNamespace" in data:
        out["session_data_namespace"] = data["sessionDataNamespace"]
    return out
