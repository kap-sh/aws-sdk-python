"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme


class UpdateThemeResponse(TypedDict, closed=True):
    entity: NotRequired["capo_amplifyuibuilder.types.theme.Theme"]
    """<p>Describes the configuration of the updated theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_amplifyuibuilder.types.theme

        out["entity"] = capo_amplifyuibuilder.types.theme.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeResponse:
    out: UpdateThemeResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import capo_amplifyuibuilder.types.theme

        out["entity"] = capo_amplifyuibuilder.types.theme.deserialize_json(
            data["entity"]
        )
    return out
