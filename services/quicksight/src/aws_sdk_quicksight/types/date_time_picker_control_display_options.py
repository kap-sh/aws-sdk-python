"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimePickerControlDisplayOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_format
    import aws_sdk_quicksight.types.label_options
    import aws_sdk_quicksight.types.sheet_control_info_icon_label_options
    import aws_sdk_quicksight.types.visibility


class DateTimePickerControlDisplayOptions(TypedDict):
    title_options: NotRequired["aws_sdk_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    date_time_format: NotRequired[
        "aws_sdk_quicksight.types.date_time_format.DateTimeFormat"
    ]
    """<p>Customize how dates are formatted in controls.</p>"""
    info_icon_label_options: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""
    helper_text_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>The helper text visibility of the <code>DateTimePickerControlDisplayOptions</code>.</p>"""
    date_icon_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The date icon visibility of the <code>DateTimePickerControlDisplayOptions</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimePickerControlDisplayOptions) -> dict:
    out: dict = {}
    if "title_options" in value:
        import aws_sdk_quicksight.types.label_options

        out["TitleOptions"] = aws_sdk_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "date_time_format" in value:
        out["DateTimeFormat"] = value["date_time_format"]
    if "info_icon_label_options" in value:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    if "helper_text_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["HelperTextVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["helper_text_visibility"]
            )
        )
    if "date_icon_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["DateIconVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["date_icon_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DateTimePickerControlDisplayOptions:
    out: DateTimePickerControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if "TitleOptions" in data:
        import aws_sdk_quicksight.types.label_options

        out["title_options"] = aws_sdk_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if "DateTimeFormat" in data:
        out["date_time_format"] = data["DateTimeFormat"]
    if "InfoIconLabelOptions" in data:
        import aws_sdk_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            aws_sdk_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    if "HelperTextVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["helper_text_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["HelperTextVisibility"]
            )
        )
    if "DateIconVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["date_icon_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["DateIconVisibility"]
            )
        )
    return out
