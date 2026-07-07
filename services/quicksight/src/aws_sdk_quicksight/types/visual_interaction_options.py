"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualInteractionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.context_menu_option
    import aws_sdk_quicksight.types.visual_menu_option


class VisualInteractionOptions(TypedDict, closed=True):
    visual_menu_option: NotRequired[
        "aws_sdk_quicksight.types.visual_menu_option.VisualMenuOption"
    ]
    """<p>The on-visual menu options for a visual.</p>"""
    context_menu_option: NotRequired[
        "aws_sdk_quicksight.types.context_menu_option.ContextMenuOption"
    ]
    """<p>The context menu options for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualInteractionOptions) -> dict:
    out: dict = {}
    if "visual_menu_option" in value:
        import aws_sdk_quicksight.types.visual_menu_option

        out["VisualMenuOption"] = (
            aws_sdk_quicksight.types.visual_menu_option.serialize_json(
                value["visual_menu_option"]
            )
        )
    if "context_menu_option" in value:
        import aws_sdk_quicksight.types.context_menu_option

        out["ContextMenuOption"] = (
            aws_sdk_quicksight.types.context_menu_option.serialize_json(
                value["context_menu_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualInteractionOptions:
    out: VisualInteractionOptions = {}  # type: ignore[typeddict-item]
    if "VisualMenuOption" in data:
        import aws_sdk_quicksight.types.visual_menu_option

        out["visual_menu_option"] = (
            aws_sdk_quicksight.types.visual_menu_option.deserialize_json(
                data["VisualMenuOption"]
            )
        )
    if "ContextMenuOption" in data:
        import aws_sdk_quicksight.types.context_menu_option

        out["context_menu_option"] = (
            aws_sdk_quicksight.types.context_menu_option.deserialize_json(
                data["ContextMenuOption"]
            )
        )
    return out
