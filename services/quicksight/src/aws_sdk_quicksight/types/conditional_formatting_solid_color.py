"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingSolidColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.hex_color


class ConditionalFormattingSolidColor(TypedDict):
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression that determines the formatting configuration for solid color.</p>"""
    color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingSolidColor) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> ConditionalFormattingSolidColor:
    out: ConditionalFormattingSolidColor = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError(
            "ConditionalFormattingSolidColor.expression required"
        )
    if "Color" in data:
        out["color"] = data["Color"]
    return out
