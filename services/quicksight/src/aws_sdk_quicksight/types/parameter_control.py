"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.parameter_date_time_picker_control
    import aws_sdk_quicksight.types.parameter_drop_down_control
    import aws_sdk_quicksight.types.parameter_list_control
    import aws_sdk_quicksight.types.parameter_slider_control
    import aws_sdk_quicksight.types.parameter_text_area_control
    import aws_sdk_quicksight.types.parameter_text_field_control


class ParameterControl(TypedDict):
    date_time_picker: NotRequired[
        "aws_sdk_quicksight.types.parameter_date_time_picker_control.ParameterDateTimePickerControl"
    ]
    """<p>A control from a date parameter that specifies date and time.</p>"""
    list: NotRequired[
        "aws_sdk_quicksight.types.parameter_list_control.ParameterListControl"
    ]
    """<p>A control to display a list with buttons or boxes that are used to select either a single value or multiple values.</p>"""
    dropdown: NotRequired[
        "aws_sdk_quicksight.types.parameter_drop_down_control.ParameterDropDownControl"
    ]
    """<p>A control to display a dropdown list with buttons that are used to select a single value.</p>"""
    text_field: NotRequired[
        "aws_sdk_quicksight.types.parameter_text_field_control.ParameterTextFieldControl"
    ]
    """<p>A control to display a text box that is used to enter a single entry.</p>"""
    text_area: NotRequired[
        "aws_sdk_quicksight.types.parameter_text_area_control.ParameterTextAreaControl"
    ]
    """<p>A control to display a text box that is used to enter multiple entries.</p>"""
    slider: NotRequired[
        "aws_sdk_quicksight.types.parameter_slider_control.ParameterSliderControl"
    ]
    """<p>A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterControl) -> dict:
    out: dict = {}
    if "date_time_picker" in value:
        import aws_sdk_quicksight.types.parameter_date_time_picker_control

        out["DateTimePicker"] = (
            aws_sdk_quicksight.types.parameter_date_time_picker_control.serialize_json(
                value["date_time_picker"]
            )
        )
    if "list" in value:
        import aws_sdk_quicksight.types.parameter_list_control

        out["List"] = aws_sdk_quicksight.types.parameter_list_control.serialize_json(
            value["list"]
        )
    if "dropdown" in value:
        import aws_sdk_quicksight.types.parameter_drop_down_control

        out["Dropdown"] = (
            aws_sdk_quicksight.types.parameter_drop_down_control.serialize_json(
                value["dropdown"]
            )
        )
    if "text_field" in value:
        import aws_sdk_quicksight.types.parameter_text_field_control

        out["TextField"] = (
            aws_sdk_quicksight.types.parameter_text_field_control.serialize_json(
                value["text_field"]
            )
        )
    if "text_area" in value:
        import aws_sdk_quicksight.types.parameter_text_area_control

        out["TextArea"] = (
            aws_sdk_quicksight.types.parameter_text_area_control.serialize_json(
                value["text_area"]
            )
        )
    if "slider" in value:
        import aws_sdk_quicksight.types.parameter_slider_control

        out["Slider"] = (
            aws_sdk_quicksight.types.parameter_slider_control.serialize_json(
                value["slider"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterControl:
    out: ParameterControl = {}  # type: ignore[typeddict-item]
    if "DateTimePicker" in data:
        import aws_sdk_quicksight.types.parameter_date_time_picker_control

        out["date_time_picker"] = (
            aws_sdk_quicksight.types.parameter_date_time_picker_control.deserialize_json(
                data["DateTimePicker"]
            )
        )
    if "List" in data:
        import aws_sdk_quicksight.types.parameter_list_control

        out["list"] = aws_sdk_quicksight.types.parameter_list_control.deserialize_json(
            data["List"]
        )
    if "Dropdown" in data:
        import aws_sdk_quicksight.types.parameter_drop_down_control

        out["dropdown"] = (
            aws_sdk_quicksight.types.parameter_drop_down_control.deserialize_json(
                data["Dropdown"]
            )
        )
    if "TextField" in data:
        import aws_sdk_quicksight.types.parameter_text_field_control

        out["text_field"] = (
            aws_sdk_quicksight.types.parameter_text_field_control.deserialize_json(
                data["TextField"]
            )
        )
    if "TextArea" in data:
        import aws_sdk_quicksight.types.parameter_text_area_control

        out["text_area"] = (
            aws_sdk_quicksight.types.parameter_text_area_control.deserialize_json(
                data["TextArea"]
            )
        )
    if "Slider" in data:
        import aws_sdk_quicksight.types.parameter_slider_control

        out["slider"] = (
            aws_sdk_quicksight.types.parameter_slider_control.deserialize_json(
                data["Slider"]
            )
        )
    return out
