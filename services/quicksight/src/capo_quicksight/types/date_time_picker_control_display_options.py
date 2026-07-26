"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimePickerControlDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_format
    import capo_quicksight.types.label_options
    import capo_quicksight.types.sheet_control_info_icon_label_options
    import capo_quicksight.types.visibility


class DateTimePickerControlDisplayOptions(TypedDict, closed=True):
    title_options: NotRequired["capo_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    date_time_format: NotRequired[
        "capo_quicksight.types.date_time_format.DateTimeFormat"
    ]
    """<p>Customize how dates are formatted in controls.</p>"""
    info_icon_label_options: NotRequired[
        "capo_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""
    helper_text_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The helper text visibility of the <code>DateTimePickerControlDisplayOptions</code>.</p>"""
    date_icon_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The date icon visibility of the <code>DateTimePickerControlDisplayOptions</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimePickerControlDisplayOptions) -> dict:
    out: dict = {}
    if "title_options" in value:
        import capo_quicksight.types.label_options

        out["TitleOptions"] = capo_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "date_time_format" in value:
        out["DateTimeFormat"] = value["date_time_format"]
    if "info_icon_label_options" in value:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    if "helper_text_visibility" in value:
        import capo_quicksight.types.visibility

        out["HelperTextVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["helper_text_visibility"]
        )
    if "date_icon_visibility" in value:
        import capo_quicksight.types.visibility

        out["DateIconVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["date_icon_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DateTimePickerControlDisplayOptions:
    out: DateTimePickerControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if "TitleOptions" in data:
        import capo_quicksight.types.label_options

        out["title_options"] = capo_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if "DateTimeFormat" in data:
        out["date_time_format"] = data["DateTimeFormat"]
    if "InfoIconLabelOptions" in data:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    if "HelperTextVisibility" in data:
        import capo_quicksight.types.visibility

        out["helper_text_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["HelperTextVisibility"]
            )
        )
    if "DateIconVisibility" in data:
        import capo_quicksight.types.visibility

        out["date_icon_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["DateIconVisibility"]
        )
    return out
