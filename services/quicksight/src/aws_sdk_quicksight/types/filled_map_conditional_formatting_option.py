"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormattingOption``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_shape_conditional_formatting


class FilledMapConditionalFormattingOption(TypedDict):
    shape: "aws_sdk_quicksight.types.filled_map_shape_conditional_formatting.FilledMapShapeConditionalFormatting"
    """<p>The conditional formatting that determines the shape of the filled map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormattingOption) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.filled_map_shape_conditional_formatting

    out["Shape"] = (
        aws_sdk_quicksight.types.filled_map_shape_conditional_formatting.serialize_json(
            value["shape"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilledMapConditionalFormattingOption:
    out: FilledMapConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "Shape" in data:
        import aws_sdk_quicksight.types.filled_map_shape_conditional_formatting

        out["shape"] = (
            aws_sdk_quicksight.types.filled_map_shape_conditional_formatting.deserialize_json(
                data["Shape"]
            )
        )
    else:
        raise DeserializationError(
            "FilledMapConditionalFormattingOption.shape required"
        )
    return out
