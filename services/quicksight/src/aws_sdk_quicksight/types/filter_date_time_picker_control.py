"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterDateTimePickerControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.commit_mode
    import aws_sdk_quicksight.types.control_title_format_text
    import aws_sdk_quicksight.types.date_time_picker_control_display_options
    import aws_sdk_quicksight.types.sheet_control_date_time_picker_type
    import aws_sdk_quicksight.types.sheet_control_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class FilterDateTimePickerControl(TypedDict):
    filter_control_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the <code>FilterDateTimePickerControl</code>.</p>"""
    title: "aws_sdk_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterDateTimePickerControl</code>.</p>"""
    source_filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The source filter ID of the <code>FilterDateTimePickerControl</code>.</p>"""
    display_options: NotRequired[
        "aws_sdk_quicksight.types.date_time_picker_control_display_options.DateTimePickerControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_date_time_picker_type.SheetControlDateTimePickerType"
    ]
    """<p>The type of the <code>FilterDropDownControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from a dropdown menu.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from a dropdown menu.</p> </li> </ul>"""
    commit_mode: NotRequired["aws_sdk_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configurationof the Apply button on a <code>DateTimePickerControl</code>.</p>"""
    control_title_format_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterDateTimePickerControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "display_options" in value:
        import aws_sdk_quicksight.types.date_time_picker_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.date_time_picker_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import aws_sdk_quicksight.types.sheet_control_date_time_picker_type

        out["Type"] = (
            aws_sdk_quicksight.types.sheet_control_date_time_picker_type.serialize_json(
                value["type"]
            )
        )
    if "commit_mode" in value:
        import aws_sdk_quicksight.types.commit_mode

        out["CommitMode"] = aws_sdk_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    if "control_title_format_text" in value:
        import aws_sdk_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            aws_sdk_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterDateTimePickerControl:
    out: FilterDateTimePickerControl = {}  # type: ignore[typeddict-item]
    if "FilterControlId" in data:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        raise DeserializationError(
            "FilterDateTimePickerControl.filter_control_id required"
        )
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceFilterId" in data:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        raise DeserializationError(
            "FilterDateTimePickerControl.source_filter_id required"
        )
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.date_time_picker_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.date_time_picker_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.sheet_control_date_time_picker_type

        out["type"] = (
            aws_sdk_quicksight.types.sheet_control_date_time_picker_type.deserialize_json(
                data["Type"]
            )
        )
    if "CommitMode" in data:
        import aws_sdk_quicksight.types.commit_mode

        out["commit_mode"] = aws_sdk_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    if "ControlTitleFormatText" in data:
        import aws_sdk_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            aws_sdk_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
