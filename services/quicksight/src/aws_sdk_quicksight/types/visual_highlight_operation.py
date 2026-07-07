"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualHighlightOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visual_highlight_trigger


class VisualHighlightOperation(TypedDict, closed=True):
    trigger: "aws_sdk_quicksight.types.visual_highlight_trigger.VisualHighlightTrigger"
    """<p>Specifies whether a highlight operation is initiated by a click or hover, or whether it's disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualHighlightOperation) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.visual_highlight_trigger

    out["Trigger"] = aws_sdk_quicksight.types.visual_highlight_trigger.serialize_json(
        value["trigger"]
    )
    return out


def deserialize_json(data: dict) -> VisualHighlightOperation:
    out: VisualHighlightOperation = {}  # type: ignore[typeddict-item]
    if "Trigger" in data:
        import aws_sdk_quicksight.types.visual_highlight_trigger

        out["trigger"] = (
            aws_sdk_quicksight.types.visual_highlight_trigger.deserialize_json(
                data["Trigger"]
            )
        )
    else:
        raise DeserializationError("VisualHighlightOperation.trigger required")
    return out
