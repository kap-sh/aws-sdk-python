"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageTooltipConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image_tooltip_text
    import aws_sdk_quicksight.types.visibility


class SheetImageTooltipConfiguration(TypedDict):
    tooltip_text: NotRequired[
        "aws_sdk_quicksight.types.sheet_image_tooltip_text.SheetImageTooltipText"
    ]
    """<p>The text that appears in the tooltip.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the tooltip.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageTooltipConfiguration) -> dict:
    out: dict = {}
    if "tooltip_text" in value:
        import aws_sdk_quicksight.types.sheet_image_tooltip_text

        out["TooltipText"] = (
            aws_sdk_quicksight.types.sheet_image_tooltip_text.serialize_json(
                value["tooltip_text"]
            )
        )
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> SheetImageTooltipConfiguration:
    out: SheetImageTooltipConfiguration = {}  # type: ignore[typeddict-item]
    if "TooltipText" in data:
        import aws_sdk_quicksight.types.sheet_image_tooltip_text

        out["tooltip_text"] = (
            aws_sdk_quicksight.types.sheet_image_tooltip_text.deserialize_json(
                data["TooltipText"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
