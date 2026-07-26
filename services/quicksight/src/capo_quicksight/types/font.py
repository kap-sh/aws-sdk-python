"""Generated from Smithy shape ``com.amazonaws.quicksight#Font``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string


class Font(TypedDict, closed=True):
    font_family: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>Determines the font family settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Font) -> dict:
    out: dict = {}
    if "font_family" in value:
        out["FontFamily"] = value["font_family"]
    return out


def deserialize_json(data: dict) -> Font:
    out: Font = {}  # type: ignore[typeddict-item]
    if "FontFamily" in data:
        out["font_family"] = data["FontFamily"]
    return out
