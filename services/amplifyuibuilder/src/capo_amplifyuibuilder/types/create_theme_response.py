"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme


class CreateThemeResponse(TypedDict, closed=True):
    entity: NotRequired["capo_amplifyuibuilder.types.theme.Theme"]
    """<p>Describes the configuration of the new theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_amplifyuibuilder.types.theme

        out["entity"] = capo_amplifyuibuilder.types.theme.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> CreateThemeResponse:
    out: CreateThemeResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import capo_amplifyuibuilder.types.theme

        out["entity"] = capo_amplifyuibuilder.types.theme.deserialize_json(
            data["entity"]
        )
    return out
