"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFilterControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.default_date_time_picker_control_options
    import aws_sdk_quicksight.types.default_filter_drop_down_control_options
    import aws_sdk_quicksight.types.default_filter_list_control_options
    import aws_sdk_quicksight.types.default_relative_date_time_control_options
    import aws_sdk_quicksight.types.default_slider_control_options
    import aws_sdk_quicksight.types.default_text_area_control_options
    import aws_sdk_quicksight.types.default_text_field_control_options


class DefaultFilterControlOptions(TypedDict, closed=True):
    default_date_time_picker_options: NotRequired[
        "aws_sdk_quicksight.types.default_date_time_picker_control_options.DefaultDateTimePickerControlOptions"
    ]
    """<p>The default options that correspond to the filter control type of a <code>DateTimePicker</code>.</p>"""
    default_list_options: NotRequired[
        "aws_sdk_quicksight.types.default_filter_list_control_options.DefaultFilterListControlOptions"
    ]
    """<p>The default options that correspond to the <code>List</code> filter control type.</p>"""
    default_dropdown_options: NotRequired[
        "aws_sdk_quicksight.types.default_filter_drop_down_control_options.DefaultFilterDropDownControlOptions"
    ]
    """<p>The default options that correspond to the <code>Dropdown</code> filter control type.</p>"""
    default_text_field_options: NotRequired[
        "aws_sdk_quicksight.types.default_text_field_control_options.DefaultTextFieldControlOptions"
    ]
    """<p>The default options that correspond to the <code>TextField</code> filter control type.</p>"""
    default_text_area_options: NotRequired[
        "aws_sdk_quicksight.types.default_text_area_control_options.DefaultTextAreaControlOptions"
    ]
    """<p>The default options that correspond to the <code>TextArea</code> filter control type.</p>"""
    default_slider_options: NotRequired[
        "aws_sdk_quicksight.types.default_slider_control_options.DefaultSliderControlOptions"
    ]
    """<p>The default options that correspond to the <code>Slider</code> filter control type.</p>"""
    default_relative_date_time_options: NotRequired[
        "aws_sdk_quicksight.types.default_relative_date_time_control_options.DefaultRelativeDateTimeControlOptions"
    ]
    """<p>The default options that correspond to the <code>RelativeDateTime</code> filter control type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFilterControlOptions) -> dict:
    out: dict = {}
    if "default_date_time_picker_options" in value:
        import aws_sdk_quicksight.types.default_date_time_picker_control_options

        out["DefaultDateTimePickerOptions"] = (
            aws_sdk_quicksight.types.default_date_time_picker_control_options.serialize_json(
                value["default_date_time_picker_options"]
            )
        )
    if "default_list_options" in value:
        import aws_sdk_quicksight.types.default_filter_list_control_options

        out["DefaultListOptions"] = (
            aws_sdk_quicksight.types.default_filter_list_control_options.serialize_json(
                value["default_list_options"]
            )
        )
    if "default_dropdown_options" in value:
        import aws_sdk_quicksight.types.default_filter_drop_down_control_options

        out["DefaultDropdownOptions"] = (
            aws_sdk_quicksight.types.default_filter_drop_down_control_options.serialize_json(
                value["default_dropdown_options"]
            )
        )
    if "default_text_field_options" in value:
        import aws_sdk_quicksight.types.default_text_field_control_options

        out["DefaultTextFieldOptions"] = (
            aws_sdk_quicksight.types.default_text_field_control_options.serialize_json(
                value["default_text_field_options"]
            )
        )
    if "default_text_area_options" in value:
        import aws_sdk_quicksight.types.default_text_area_control_options

        out["DefaultTextAreaOptions"] = (
            aws_sdk_quicksight.types.default_text_area_control_options.serialize_json(
                value["default_text_area_options"]
            )
        )
    if "default_slider_options" in value:
        import aws_sdk_quicksight.types.default_slider_control_options

        out["DefaultSliderOptions"] = (
            aws_sdk_quicksight.types.default_slider_control_options.serialize_json(
                value["default_slider_options"]
            )
        )
    if "default_relative_date_time_options" in value:
        import aws_sdk_quicksight.types.default_relative_date_time_control_options

        out["DefaultRelativeDateTimeOptions"] = (
            aws_sdk_quicksight.types.default_relative_date_time_control_options.serialize_json(
                value["default_relative_date_time_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFilterControlOptions:
    out: DefaultFilterControlOptions = {}  # type: ignore[typeddict-item]
    if "DefaultDateTimePickerOptions" in data:
        import aws_sdk_quicksight.types.default_date_time_picker_control_options

        out["default_date_time_picker_options"] = (
            aws_sdk_quicksight.types.default_date_time_picker_control_options.deserialize_json(
                data["DefaultDateTimePickerOptions"]
            )
        )
    if "DefaultListOptions" in data:
        import aws_sdk_quicksight.types.default_filter_list_control_options

        out["default_list_options"] = (
            aws_sdk_quicksight.types.default_filter_list_control_options.deserialize_json(
                data["DefaultListOptions"]
            )
        )
    if "DefaultDropdownOptions" in data:
        import aws_sdk_quicksight.types.default_filter_drop_down_control_options

        out["default_dropdown_options"] = (
            aws_sdk_quicksight.types.default_filter_drop_down_control_options.deserialize_json(
                data["DefaultDropdownOptions"]
            )
        )
    if "DefaultTextFieldOptions" in data:
        import aws_sdk_quicksight.types.default_text_field_control_options

        out["default_text_field_options"] = (
            aws_sdk_quicksight.types.default_text_field_control_options.deserialize_json(
                data["DefaultTextFieldOptions"]
            )
        )
    if "DefaultTextAreaOptions" in data:
        import aws_sdk_quicksight.types.default_text_area_control_options

        out["default_text_area_options"] = (
            aws_sdk_quicksight.types.default_text_area_control_options.deserialize_json(
                data["DefaultTextAreaOptions"]
            )
        )
    if "DefaultSliderOptions" in data:
        import aws_sdk_quicksight.types.default_slider_control_options

        out["default_slider_options"] = (
            aws_sdk_quicksight.types.default_slider_control_options.deserialize_json(
                data["DefaultSliderOptions"]
            )
        )
    if "DefaultRelativeDateTimeOptions" in data:
        import aws_sdk_quicksight.types.default_relative_date_time_control_options

        out["default_relative_date_time_options"] = (
            aws_sdk_quicksight.types.default_relative_date_time_control_options.deserialize_json(
                data["DefaultRelativeDateTimeOptions"]
            )
        )
    return out
