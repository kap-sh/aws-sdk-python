"""Generated from Smithy shape ``com.amazonaws.pinpoint#DefaultButtonConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.button_action


class DefaultButtonConfiguration(TypedDict, closed=True):
    background_color: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The background color of the button.</p>"""
    border_radius: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The border radius of the button.</p>"""
    button_action: NotRequired["capo_pinpoint.types.button_action.ButtonAction"]
    """<p>Action triggered by the button.</p>"""
    link: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Button destination.</p>"""
    text: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Button text.</p>"""
    text_color: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The text color of the button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultButtonConfiguration) -> dict:
    out: dict = {}
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    if "border_radius" in value:
        out["BorderRadius"] = value["border_radius"]
    if "button_action" in value:
        import capo_pinpoint.types.button_action

        out["ButtonAction"] = capo_pinpoint.types.button_action.serialize_json(
            value["button_action"]
        )
    if "link" in value:
        out["Link"] = value["link"]
    if "text" in value:
        out["Text"] = value["text"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> DefaultButtonConfiguration:
    out: DefaultButtonConfiguration = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    if "BorderRadius" in data:
        out["border_radius"] = data["BorderRadius"]
    if "ButtonAction" in data:
        import capo_pinpoint.types.button_action

        out["button_action"] = capo_pinpoint.types.button_action.deserialize_json(
            data["ButtonAction"]
        )
    if "Link" in data:
        out["link"] = data["Link"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "TextColor" in data:
        out["text_color"] = data["TextColor"]
    return out
