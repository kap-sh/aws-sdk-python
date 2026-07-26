"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.update_theme_data
    import capo_amplifyuibuilder.types.uuid


class UpdateThemeRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the theme.</p>"""
    client_token: NotRequired["str"]
    """<p>The unique client token.</p>"""
    updated_theme: "capo_amplifyuibuilder.types.update_theme_data.UpdateThemeData"
    """<p>The configuration of the updated theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.update_theme_data

    out["updatedTheme"] = capo_amplifyuibuilder.types.update_theme_data.serialize_json(
        value["updated_theme"]
    )
    return out


def deserialize_json(data: dict) -> UpdateThemeRequest:
    out: UpdateThemeRequest = {}  # type: ignore[typeddict-item]
    if "updatedTheme" in data:
        import capo_amplifyuibuilder.types.update_theme_data

        out["updated_theme"] = (
            capo_amplifyuibuilder.types.update_theme_data.deserialize_json(
                data["updatedTheme"]
            )
        )
    else:
        raise DeserializationError("UpdateThemeRequest.updated_theme required")
    return out
