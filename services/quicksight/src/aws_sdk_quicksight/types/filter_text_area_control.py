"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterTextAreaControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_format_text
    import aws_sdk_quicksight.types.sheet_control_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.text_area_control_delimiter
    import aws_sdk_quicksight.types.text_area_control_display_options


class FilterTextAreaControl(TypedDict):
    filter_control_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the <code>FilterTextAreaControl</code>.</p>"""
    title: "aws_sdk_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterTextAreaControl</code>.</p>"""
    source_filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The source filter ID of the <code>FilterTextAreaControl</code>.</p>"""
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
def serialize_json(value: FilterTextAreaControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
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


def deserialize_json(data: dict) -> FilterTextAreaControl:
    out: FilterTextAreaControl = {}  # type: ignore[typeddict-item]
    if "FilterControlId" in data:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        raise DeserializationError("FilterTextAreaControl.filter_control_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceFilterId" in data:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        raise DeserializationError("FilterTextAreaControl.source_filter_id required")
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
