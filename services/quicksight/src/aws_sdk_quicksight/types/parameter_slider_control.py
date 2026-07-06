"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterSliderControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_format_text
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.sheet_control_title
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.slider_control_display_options


class ParameterSliderControl(TypedDict, closed=True):
    parameter_control_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the <code>ParameterSliderControl</code>.</p>"""
    title: "aws_sdk_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>ParameterSliderControl</code>.</p>"""
    source_parameter_name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The source parameter name of the <code>ParameterSliderControl</code>.</p>"""
    display_options: NotRequired[
        "aws_sdk_quicksight.types.slider_control_display_options.SliderControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    maximum_value: "aws_sdk_quicksight.types.double.Double"
    """<p>The larger value that is displayed at the right of the slider.</p>"""
    minimum_value: "aws_sdk_quicksight.types.double.Double"
    """<p>The smaller value that is displayed at the left of the slider.</p>"""
    step_size: "aws_sdk_quicksight.types.double.Double"
    """<p>The number of increments that the slider bar is divided into.</p>"""
    control_title_format_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSliderControl) -> dict:
    out: dict = {}
    out["ParameterControlId"] = value["parameter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceParameterName"] = value["source_parameter_name"]
    if "display_options" in value:
        import aws_sdk_quicksight.types.slider_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.slider_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    out["MaximumValue"] = value.get("maximum_value", 0)
    out["MinimumValue"] = value.get("minimum_value", 0)
    out["StepSize"] = value.get("step_size", 0)
    if "control_title_format_text" in value:
        import aws_sdk_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            aws_sdk_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterSliderControl:
    out: ParameterSliderControl = {}  # type: ignore[typeddict-item]
    if "ParameterControlId" in data:
        out["parameter_control_id"] = data["ParameterControlId"]
    else:
        raise DeserializationError(
            "ParameterSliderControl.parameter_control_id required"
        )
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if "SourceParameterName" in data:
        out["source_parameter_name"] = data["SourceParameterName"]
    else:
        raise DeserializationError(
            "ParameterSliderControl.source_parameter_name required"
        )
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.slider_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.slider_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "MaximumValue" in data:
        out["maximum_value"] = data["MaximumValue"]
    else:
        out["maximum_value"] = 0
    if "MinimumValue" in data:
        out["minimum_value"] = data["MinimumValue"]
    else:
        out["minimum_value"] = 0
    if "StepSize" in data:
        out["step_size"] = data["StepSize"]
    else:
        out["step_size"] = 0
    if "ControlTitleFormatText" in data:
        import aws_sdk_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            aws_sdk_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
