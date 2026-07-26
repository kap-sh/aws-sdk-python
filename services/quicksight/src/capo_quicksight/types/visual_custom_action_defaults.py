"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visual_highlight_operation


class VisualCustomActionDefaults(TypedDict, closed=True):
    highlight_operation: NotRequired[
        "capo_quicksight.types.visual_highlight_operation.VisualHighlightOperation"
    ]
    """<p>A list of highlight operations available for visuals in an analysis or sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionDefaults) -> dict:
    out: dict = {}
    if "highlight_operation" in value:
        import capo_quicksight.types.visual_highlight_operation

        out["highlightOperation"] = (
            capo_quicksight.types.visual_highlight_operation.serialize_json(
                value["highlight_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualCustomActionDefaults:
    out: VisualCustomActionDefaults = {}  # type: ignore[typeddict-item]
    if "highlightOperation" in data:
        import capo_quicksight.types.visual_highlight_operation

        out["highlight_operation"] = (
            capo_quicksight.types.visual_highlight_operation.deserialize_json(
                data["highlightOperation"]
            )
        )
    return out
