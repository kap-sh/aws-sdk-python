"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideInputValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.tool_override_input_value_configuration


class ToolOverrideInputValue(TypedDict, closed=True):
    json_path: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The JSON path for the input value override.</p>"""
    value: "aws_sdk_qconnect.types.tool_override_input_value_configuration.ToolOverrideInputValueConfiguration"
    """<p>The override input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideInputValue) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    import aws_sdk_qconnect.types.tool_override_input_value_configuration

    out["value"] = (
        aws_sdk_qconnect.types.tool_override_input_value_configuration.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolOverrideInputValue:
    out: ToolOverrideInputValue = {}  # type: ignore[typeddict-item]
    if "jsonPath" in data:
        out["json_path"] = data["jsonPath"]
    else:
        raise DeserializationError("ToolOverrideInputValue.json_path required")
    if "value" in data:
        import aws_sdk_qconnect.types.tool_override_input_value_configuration

        out["value"] = (
            aws_sdk_qconnect.types.tool_override_input_value_configuration.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("ToolOverrideInputValue.value required")
    return out
