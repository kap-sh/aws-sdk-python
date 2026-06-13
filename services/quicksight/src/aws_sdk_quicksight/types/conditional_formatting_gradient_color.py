"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingGradientColor``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.gradient_color


class ConditionalFormattingGradientColor(TypedDict):
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression that determines the formatting configuration for gradient color.</p>"""
    color: "aws_sdk_quicksight.types.gradient_color.GradientColor"
    """<p>Determines the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingGradientColor) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import aws_sdk_quicksight.types.gradient_color

    out["Color"] = aws_sdk_quicksight.types.gradient_color.serialize_json(
        value["color"]
    )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingGradientColor:
    out: ConditionalFormattingGradientColor = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError(
            "ConditionalFormattingGradientColor.expression required"
        )
    if "Color" in data:
        import aws_sdk_quicksight.types.gradient_color

        out["color"] = aws_sdk_quicksight.types.gradient_color.deserialize_json(
            data["Color"]
        )
    else:
        raise DeserializationError("ConditionalFormattingGradientColor.color required")
    return out
