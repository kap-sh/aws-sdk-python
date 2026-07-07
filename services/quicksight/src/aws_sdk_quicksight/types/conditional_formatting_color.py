"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_gradient_color
    import aws_sdk_quicksight.types.conditional_formatting_solid_color


class ConditionalFormattingColor(TypedDict, closed=True):
    solid: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_solid_color.ConditionalFormattingSolidColor"
    ]
    """<p>Formatting configuration for solid color.</p>"""
    gradient: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_gradient_color.ConditionalFormattingGradientColor"
    ]
    """<p>Formatting configuration for gradient color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingColor) -> dict:
    out: dict = {}
    if "solid" in value:
        import aws_sdk_quicksight.types.conditional_formatting_solid_color

        out["Solid"] = (
            aws_sdk_quicksight.types.conditional_formatting_solid_color.serialize_json(
                value["solid"]
            )
        )
    if "gradient" in value:
        import aws_sdk_quicksight.types.conditional_formatting_gradient_color

        out["Gradient"] = (
            aws_sdk_quicksight.types.conditional_formatting_gradient_color.serialize_json(
                value["gradient"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingColor:
    out: ConditionalFormattingColor = {}  # type: ignore[typeddict-item]
    if "Solid" in data:
        import aws_sdk_quicksight.types.conditional_formatting_solid_color

        out["solid"] = (
            aws_sdk_quicksight.types.conditional_formatting_solid_color.deserialize_json(
                data["Solid"]
            )
        )
    if "Gradient" in data:
        import aws_sdk_quicksight.types.conditional_formatting_gradient_color

        out["gradient"] = (
            aws_sdk_quicksight.types.conditional_formatting_gradient_color.deserialize_json(
                data["Gradient"]
            )
        )
    return out
