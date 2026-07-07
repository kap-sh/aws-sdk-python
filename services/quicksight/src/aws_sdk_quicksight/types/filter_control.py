"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_cross_sheet_control
    import aws_sdk_quicksight.types.filter_date_time_picker_control
    import aws_sdk_quicksight.types.filter_drop_down_control
    import aws_sdk_quicksight.types.filter_list_control
    import aws_sdk_quicksight.types.filter_relative_date_time_control
    import aws_sdk_quicksight.types.filter_slider_control
    import aws_sdk_quicksight.types.filter_text_area_control
    import aws_sdk_quicksight.types.filter_text_field_control


class FilterControl(TypedDict, closed=True):
    date_time_picker: NotRequired[
        "aws_sdk_quicksight.types.filter_date_time_picker_control.FilterDateTimePickerControl"
    ]
    """<p>A control from a date filter that is used to specify date and time.</p>"""
    list: NotRequired["aws_sdk_quicksight.types.filter_list_control.FilterListControl"]
    """<p>A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.</p>"""
    dropdown: NotRequired[
        "aws_sdk_quicksight.types.filter_drop_down_control.FilterDropDownControl"
    ]
    """<p>A control to display a dropdown list with buttons that are used to select a single value.</p>"""
    text_field: NotRequired[
        "aws_sdk_quicksight.types.filter_text_field_control.FilterTextFieldControl"
    ]
    """<p>A control to display a text box that is used to enter a single entry.</p>"""
    text_area: NotRequired[
        "aws_sdk_quicksight.types.filter_text_area_control.FilterTextAreaControl"
    ]
    """<p>A control to display a text box that is used to enter multiple entries.</p>"""
    slider: NotRequired[
        "aws_sdk_quicksight.types.filter_slider_control.FilterSliderControl"
    ]
    """<p>A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.</p>"""
    relative_date_time: NotRequired[
        "aws_sdk_quicksight.types.filter_relative_date_time_control.FilterRelativeDateTimeControl"
    ]
    """<p>A control from a date filter that is used to specify the relative date.</p>"""
    cross_sheet: NotRequired[
        "aws_sdk_quicksight.types.filter_cross_sheet_control.FilterCrossSheetControl"
    ]
    """<p>A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterControl) -> dict:
    out: dict = {}
    if "date_time_picker" in value:
        import aws_sdk_quicksight.types.filter_date_time_picker_control

        out["DateTimePicker"] = (
            aws_sdk_quicksight.types.filter_date_time_picker_control.serialize_json(
                value["date_time_picker"]
            )
        )
    if "list" in value:
        import aws_sdk_quicksight.types.filter_list_control

        out["List"] = aws_sdk_quicksight.types.filter_list_control.serialize_json(
            value["list"]
        )
    if "dropdown" in value:
        import aws_sdk_quicksight.types.filter_drop_down_control

        out["Dropdown"] = (
            aws_sdk_quicksight.types.filter_drop_down_control.serialize_json(
                value["dropdown"]
            )
        )
    if "text_field" in value:
        import aws_sdk_quicksight.types.filter_text_field_control

        out["TextField"] = (
            aws_sdk_quicksight.types.filter_text_field_control.serialize_json(
                value["text_field"]
            )
        )
    if "text_area" in value:
        import aws_sdk_quicksight.types.filter_text_area_control

        out["TextArea"] = (
            aws_sdk_quicksight.types.filter_text_area_control.serialize_json(
                value["text_area"]
            )
        )
    if "slider" in value:
        import aws_sdk_quicksight.types.filter_slider_control

        out["Slider"] = aws_sdk_quicksight.types.filter_slider_control.serialize_json(
            value["slider"]
        )
    if "relative_date_time" in value:
        import aws_sdk_quicksight.types.filter_relative_date_time_control

        out["RelativeDateTime"] = (
            aws_sdk_quicksight.types.filter_relative_date_time_control.serialize_json(
                value["relative_date_time"]
            )
        )
    if "cross_sheet" in value:
        import aws_sdk_quicksight.types.filter_cross_sheet_control

        out["CrossSheet"] = (
            aws_sdk_quicksight.types.filter_cross_sheet_control.serialize_json(
                value["cross_sheet"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterControl:
    out: FilterControl = {}  # type: ignore[typeddict-item]
    if "DateTimePicker" in data:
        import aws_sdk_quicksight.types.filter_date_time_picker_control

        out["date_time_picker"] = (
            aws_sdk_quicksight.types.filter_date_time_picker_control.deserialize_json(
                data["DateTimePicker"]
            )
        )
    if "List" in data:
        import aws_sdk_quicksight.types.filter_list_control

        out["list"] = aws_sdk_quicksight.types.filter_list_control.deserialize_json(
            data["List"]
        )
    if "Dropdown" in data:
        import aws_sdk_quicksight.types.filter_drop_down_control

        out["dropdown"] = (
            aws_sdk_quicksight.types.filter_drop_down_control.deserialize_json(
                data["Dropdown"]
            )
        )
    if "TextField" in data:
        import aws_sdk_quicksight.types.filter_text_field_control

        out["text_field"] = (
            aws_sdk_quicksight.types.filter_text_field_control.deserialize_json(
                data["TextField"]
            )
        )
    if "TextArea" in data:
        import aws_sdk_quicksight.types.filter_text_area_control

        out["text_area"] = (
            aws_sdk_quicksight.types.filter_text_area_control.deserialize_json(
                data["TextArea"]
            )
        )
    if "Slider" in data:
        import aws_sdk_quicksight.types.filter_slider_control

        out["slider"] = aws_sdk_quicksight.types.filter_slider_control.deserialize_json(
            data["Slider"]
        )
    if "RelativeDateTime" in data:
        import aws_sdk_quicksight.types.filter_relative_date_time_control

        out["relative_date_time"] = (
            aws_sdk_quicksight.types.filter_relative_date_time_control.deserialize_json(
                data["RelativeDateTime"]
            )
        )
    if "CrossSheet" in data:
        import aws_sdk_quicksight.types.filter_cross_sheet_control

        out["cross_sheet"] = (
            aws_sdk_quicksight.types.filter_cross_sheet_control.deserialize_json(
                data["CrossSheet"]
            )
        )
    return out
