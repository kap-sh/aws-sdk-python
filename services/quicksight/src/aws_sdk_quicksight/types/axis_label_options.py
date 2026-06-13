"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_label_reference_options
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.string


class AxisLabelOptions(TypedDict):
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The font configuration of the axis label.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The text for the axis label.</p>"""
    apply_to: NotRequired[
        "aws_sdk_quicksight.types.axis_label_reference_options.AxisLabelReferenceOptions"
    ]
    """<p>The options that indicate which field the label belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLabelOptions) -> dict:
    out: dict = {}
    if "font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["FontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["font_configuration"]
            )
        )
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "apply_to" in value:
        import aws_sdk_quicksight.types.axis_label_reference_options

        out["ApplyTo"] = (
            aws_sdk_quicksight.types.axis_label_reference_options.serialize_json(
                value["apply_to"]
            )
        )
    return out


def deserialize_json(data: dict) -> AxisLabelOptions:
    out: AxisLabelOptions = {}  # type: ignore[typeddict-item]
    if "FontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    if "ApplyTo" in data:
        import aws_sdk_quicksight.types.axis_label_reference_options

        out["apply_to"] = (
            aws_sdk_quicksight.types.axis_label_reference_options.deserialize_json(
                data["ApplyTo"]
            )
        )
    return out
