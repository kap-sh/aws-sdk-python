"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterTextAreaControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_format_text
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.sheet_control_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.text_area_control_delimiter
    import aws_sdk_quicksight.types.text_area_control_display_options


class ParameterTextAreaControl(TypedDict, closed=True):
    parameter_control_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the <code>ParameterTextAreaControl</code>.</p>"""
    title: "aws_sdk_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>ParameterTextAreaControl</code>.</p>"""
    source_parameter_name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The source parameter name of the <code>ParameterTextAreaControl</code>.</p>"""
    delimiter: NotRequired[
        "aws_sdk_quicksight.types.text_area_control_delimiter.TextAreaControlDelimiter"
    ]
    """<p>The delimiter that is used to separate the lines in text.</p>"""
    display_options: NotRequired[
        "aws_sdk_quicksight.types.text_area_control_display_options.TextAreaControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    control_title_format_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterTextAreaControl) -> dict:
    out: dict = {}
    out["ParameterControlId"] = value["parameter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceParameterName"] = value["source_parameter_name"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "display_options" in value:
        import aws_sdk_quicksight.types.text_area_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.text_area_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "control_title_format_text" in value:
        import aws_sdk_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            aws_sdk_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterTextAreaControl:
    out: ParameterTextAreaControl = {}  # type: ignore[typeddict-item]
    if "ParameterControlId" in data:
        out["parameter_control_id"] = data["ParameterControlId"]
    else:
        raise DeserializationError(
            "ParameterTextAreaControl.parameter_control_id required"
        )
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceParameterName" in data:
        out["source_parameter_name"] = data["SourceParameterName"]
    else:
        raise DeserializationError(
            "ParameterTextAreaControl.source_parameter_name required"
        )
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.text_area_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.text_area_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "ControlTitleFormatText" in data:
        import aws_sdk_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            aws_sdk_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
