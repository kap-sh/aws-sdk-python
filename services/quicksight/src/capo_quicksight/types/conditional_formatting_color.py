"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_gradient_color
    import capo_quicksight.types.conditional_formatting_solid_color


class ConditionalFormattingColor(TypedDict, closed=True):
    solid: NotRequired[
        "capo_quicksight.types.conditional_formatting_solid_color.ConditionalFormattingSolidColor"
    ]
    """<p>Formatting configuration for solid color.</p>"""
    gradient: NotRequired[
        "capo_quicksight.types.conditional_formatting_gradient_color.ConditionalFormattingGradientColor"
    ]
    """<p>Formatting configuration for gradient color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingColor) -> dict:
    out: dict = {}
    if "solid" in value:
        import capo_quicksight.types.conditional_formatting_solid_color

        out["Solid"] = (
            capo_quicksight.types.conditional_formatting_solid_color.serialize_json(
                value["solid"]
            )
        )
    if "gradient" in value:
        import capo_quicksight.types.conditional_formatting_gradient_color

        out["Gradient"] = (
            capo_quicksight.types.conditional_formatting_gradient_color.serialize_json(
                value["gradient"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingColor:
    out: ConditionalFormattingColor = {}  # type: ignore[typeddict-item]
    if "Solid" in data:
        import capo_quicksight.types.conditional_formatting_solid_color

        out["solid"] = (
            capo_quicksight.types.conditional_formatting_solid_color.deserialize_json(
                data["Solid"]
            )
        )
    if "Gradient" in data:
        import capo_quicksight.types.conditional_formatting_gradient_color

        out["gradient"] = (
            capo_quicksight.types.conditional_formatting_gradient_color.deserialize_json(
                data["Gradient"]
            )
        )
    return out
