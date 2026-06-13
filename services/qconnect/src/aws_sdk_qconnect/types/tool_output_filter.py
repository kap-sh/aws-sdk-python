"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOutputFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.tool_output_configuration


class ToolOutputFilter(TypedDict):
    json_path: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The JSON path for filtering tool output.</p>"""
    output_configuration: NotRequired[
        "aws_sdk_qconnect.types.tool_output_configuration.ToolOutputConfiguration"
    ]
    """<p>The output configuration for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOutputFilter) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    if "output_configuration" in value:
        import aws_sdk_qconnect.types.tool_output_configuration

        out["outputConfiguration"] = (
            aws_sdk_qconnect.types.tool_output_configuration.serialize_json(
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
        import aws_sdk_qconnect.types.tool_output_configuration

        out["output_configuration"] = (
            aws_sdk_qconnect.types.tool_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    return out
