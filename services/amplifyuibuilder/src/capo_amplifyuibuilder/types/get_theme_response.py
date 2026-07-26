"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme


class GetThemeResponse(TypedDict, closed=True):
    theme: NotRequired["capo_amplifyuibuilder.types.theme.Theme"]
    """<p>Represents the configuration settings for the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThemeResponse) -> dict:
    out: dict = {}
    if "theme" in value:
        import capo_amplifyuibuilder.types.theme

        out["theme"] = capo_amplifyuibuilder.types.theme.serialize_json(value["theme"])
    return out


def deserialize_json(data: dict) -> GetThemeResponse:
    out: GetThemeResponse = {}  # type: ignore[typeddict-item]
    if "theme" in data:
        import capo_amplifyuibuilder.types.theme

        out["theme"] = capo_amplifyuibuilder.types.theme.deserialize_json(data["theme"])
    return out
