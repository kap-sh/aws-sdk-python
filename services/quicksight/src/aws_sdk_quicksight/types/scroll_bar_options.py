"""Generated from Smithy shape ``com.amazonaws.quicksight#ScrollBarOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visibility
    import aws_sdk_quicksight.types.visible_range_options


class ScrollBarOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the data zoom scroll bar.</p>"""
    visible_range: NotRequired[
        "aws_sdk_quicksight.types.visible_range_options.VisibleRangeOptions"
    ]
    """<p>The visibility range for the data zoom scroll bar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScrollBarOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "visible_range" in value:
        import aws_sdk_quicksight.types.visible_range_options

        out["VisibleRange"] = (
            aws_sdk_quicksight.types.visible_range_options.serialize_json(
                value["visible_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScrollBarOptions:
    out: ScrollBarOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "VisibleRange" in data:
        import aws_sdk_quicksight.types.visible_range_options

        out["visible_range"] = (
            aws_sdk_quicksight.types.visible_range_options.deserialize_json(
                data["VisibleRange"]
            )
        )
    return out
