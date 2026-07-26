"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOutputFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.tool_output_configuration


class ToolOutputFilter(TypedDict, closed=True):
    json_path: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The JSON path for filtering tool output.</p>"""
    output_configuration: NotRequired[
        "capo_qconnect.types.tool_output_configuration.ToolOutputConfiguration"
    ]
    """<p>The output configuration for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOutputFilter) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    if "output_configuration" in value:
        import capo_qconnect.types.tool_output_configuration

        out["outputConfiguration"] = (
            capo_qconnect.types.tool_output_configuration.serialize_json(
                value["output_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ToolOutputFilter:
    out: ToolOutputFilter = {}  # type: ignore[typeddict-item]
    if "jsonPath" in data:
        out["json_path"] = data["jsonPath"]
    else:
        raise DeserializationError("ToolOutputFilter.json_path required")
    if "outputConfiguration" in data:
        import capo_qconnect.types.tool_output_configuration

        out["output_configuration"] = (
            capo_qconnect.types.tool_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    return out
