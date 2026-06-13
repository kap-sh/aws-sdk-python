"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterTextFieldControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_format_text
    import aws_sdk_quicksight.types.sheet_control_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.text_field_control_display_options


class FilterTextFieldControl(TypedDict):
    filter_control_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the <code>FilterTextFieldControl</code>.</p>"""
    title: "aws_sdk_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterTextFieldControl</code>.</p>"""
    source_filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The source filter ID of the <code>FilterTextFieldControl</code>.</p>"""
    display_options: NotRequired[
        "aws_sdk_quicksight.types.text_field_control_display_options.TextFieldControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    control_title_format_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterTextFieldControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "display_options" in value:
        import aws_sdk_quicksight.types.text_field_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.text_field_control_display_options.serialize_json(
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


def deserialize_json(data: dict) -> FilterTextFieldControl:
    out: FilterTextFieldControl = {}  # type: ignore[typeddict-item]
    if "FilterControlId" in data:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        raise DeserializationError("FilterTextFieldControl.filter_control_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceFilterId" in data:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        raise DeserializationError("FilterTextFieldControl.source_filter_id required")
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.text_field_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.text_field_control_display_options.deserialize_json(
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
