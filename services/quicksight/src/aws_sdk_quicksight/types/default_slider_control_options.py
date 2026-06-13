"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultSliderControlOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.sheet_control_slider_type
    import aws_sdk_quicksight.types.slider_control_display_options


class DefaultSliderControlOptions(TypedDict):
    display_options: NotRequired[
        "aws_sdk_quicksight.types.slider_control_display_options.SliderControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_slider_type.SheetControlSliderType"
    ]
    """<p>The type of the <code>DefaultSliderControlOptions</code>. Choose one of the following options:</p> <ul> <li> <p> <code>SINGLE_POINT</code>: Filter against(equals) a single data point.</p> </li> <li> <p> <code>RANGE</code>: Filter data that is in a specified range.</p> </li> </ul>"""
    maximum_value: "aws_sdk_quicksight.types.double.Double"
    """<p>The larger value that is displayed at the right of the slider.</p>"""
    minimum_value: "aws_sdk_quicksight.types.double.Double"
    """<p>The smaller value that is displayed at the left of the slider.</p>"""
    step_size: "aws_sdk_quicksight.types.double.Double"
    """<p>The number of increments that the slider bar is divided into.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSliderControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import aws_sdk_quicksight.types.slider_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.slider_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import aws_sdk_quicksight.types.sheet_control_slider_type

        out["Type"] = aws_sdk_quicksight.types.sheet_control_slider_type.serialize_json(
            value["type"]
        )
    out["MaximumValue"] = value.get("maximum_value", 0)
    out["MinimumValue"] = value.get("minimum_value", 0)
    out["StepSize"] = value.get("step_size", 0)
    return out


def deserialize_json(data: dict) -> DefaultSliderControlOptions:
    out: DefaultSliderControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.slider_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.slider_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.sheet_control_slider_type

        out["type"] = (
            aws_sdk_quicksight.types.sheet_control_slider_type.deserialize_json(
                data["Type"]
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
    return out
