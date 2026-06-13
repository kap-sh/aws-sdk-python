"""Generated from Smithy shape ``com.amazonaws.quicksight#TextBoxInteractionOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.text_box_menu_option


class TextBoxInteractionOptions(TypedDict):
    text_box_menu_option: NotRequired[
        "aws_sdk_quicksight.types.text_box_menu_option.TextBoxMenuOption"
    ]
    """<p>The menu options for the textbox.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextBoxInteractionOptions) -> dict:
    out: dict = {}
    if "text_box_menu_option" in value:
        import aws_sdk_quicksight.types.text_box_menu_option

        out["TextBoxMenuOption"] = (
            aws_sdk_quicksight.types.text_box_menu_option.serialize_json(
                value["text_box_menu_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextBoxInteractionOptions:
    out: TextBoxInteractionOptions = {}  # type: ignore[typeddict-item]
    if "TextBoxMenuOption" in data:
        import aws_sdk_quicksight.types.text_box_menu_option

        out["text_box_menu_option"] = (
            aws_sdk_quicksight.types.text_box_menu_option.deserialize_json(
                data["TextBoxMenuOption"]
            )
        )
    return out
