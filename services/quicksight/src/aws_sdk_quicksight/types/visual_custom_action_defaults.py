"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionDefaults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visual_highlight_operation


class VisualCustomActionDefaults(TypedDict):
    highlight_operation: NotRequired[
        "aws_sdk_quicksight.types.visual_highlight_operation.VisualHighlightOperation"
    ]
    """<p>A list of highlight operations available for visuals in an analysis or sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionDefaults) -> dict:
    out: dict = {}
    if "highlight_operation" in value:
        import aws_sdk_quicksight.types.visual_highlight_operation

        out["highlightOperation"] = (
            aws_sdk_quicksight.types.visual_highlight_operation.serialize_json(
                value["highlight_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualCustomActionDefaults:
    out: VisualCustomActionDefaults = {}  # type: ignore[typeddict-item]
    if "highlightOperation" in data:
        import aws_sdk_quicksight.types.visual_highlight_operation

        out["highlight_operation"] = (
            aws_sdk_quicksight.types.visual_highlight_operation.deserialize_json(
                data["highlightOperation"]
            )
        )
    return out
