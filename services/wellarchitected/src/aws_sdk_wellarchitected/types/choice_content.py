"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_content_display_text
    import aws_sdk_wellarchitected.types.choice_content_url


class ChoiceContent(TypedDict):
    display_text: NotRequired[
        "aws_sdk_wellarchitected.types.choice_content_display_text.ChoiceContentDisplayText"
    ]
    """<p>The display text for the choice content.</p>"""
    url: NotRequired[
        "aws_sdk_wellarchitected.types.choice_content_url.ChoiceContentUrl"
    ]
    """<p>The URL for the choice content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceContent) -> dict:
    out: dict = {}
    if "display_text" in value:
        out["DisplayText"] = value["display_text"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ChoiceContent:
    out: ChoiceContent = {}  # type: ignore[typeddict-item]
    if "DisplayText" in data:
        out["display_text"] = data["DisplayText"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
