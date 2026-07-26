"""Generated from Smithy shape ``com.amazonaws.quicksight#TextBoxInteractionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.text_box_menu_option


class TextBoxInteractionOptions(TypedDict, closed=True):
    text_box_menu_option: NotRequired[
        "capo_quicksight.types.text_box_menu_option.TextBoxMenuOption"
    ]
    """<p>The menu options for the textbox.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextBoxInteractionOptions) -> dict:
    out: dict = {}
    if "text_box_menu_option" in value:
        import capo_quicksight.types.text_box_menu_option

        out["TextBoxMenuOption"] = (
            capo_quicksight.types.text_box_menu_option.serialize_json(
                value["text_box_menu_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextBoxInteractionOptions:
    out: TextBoxInteractionOptions = {}  # type: ignore[typeddict-item]
    if "TextBoxMenuOption" in data:
        import capo_quicksight.types.text_box_menu_option

        out["text_box_menu_option"] = (
            capo_quicksight.types.text_box_menu_option.deserialize_json(
                data["TextBoxMenuOption"]
            )
        )
    return out
