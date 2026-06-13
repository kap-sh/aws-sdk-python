"""Generated from Smithy shape ``com.amazonaws.quicksight#ShapeConditionalFormat``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color


class ShapeConditionalFormat(TypedDict):
    background_color: "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    """<p>The conditional formatting for the shape background color of a filled map visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShapeConditionalFormat) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.conditional_formatting_color

    out["BackgroundColor"] = (
        aws_sdk_quicksight.types.conditional_formatting_color.serialize_json(
            value["background_color"]
        )
    )
    return out


def deserialize_json(data: dict) -> ShapeConditionalFormat:
    out: ShapeConditionalFormat = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.deserialize_json(
                data["BackgroundColor"]
            )
        )
    else:
        raise DeserializationError("ShapeConditionalFormat.background_color required")
    return out
