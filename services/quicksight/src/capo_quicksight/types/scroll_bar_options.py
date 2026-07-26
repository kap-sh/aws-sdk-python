"""Generated from Smithy shape ``com.amazonaws.quicksight#ScrollBarOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility
    import capo_quicksight.types.visible_range_options


class ScrollBarOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the data zoom scroll bar.</p>"""
    visible_range: NotRequired[
        "capo_quicksight.types.visible_range_options.VisibleRangeOptions"
    ]
    """<p>The visibility range for the data zoom scroll bar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScrollBarOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "visible_range" in value:
        import capo_quicksight.types.visible_range_options

        out["VisibleRange"] = (
            capo_quicksight.types.visible_range_options.serialize_json(
                value["visible_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScrollBarOptions:
    out: ScrollBarOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "VisibleRange" in data:
        import capo_quicksight.types.visible_range_options

        out["visible_range"] = (
            capo_quicksight.types.visible_range_options.deserialize_json(
                data["VisibleRange"]
            )
        )
    return out
