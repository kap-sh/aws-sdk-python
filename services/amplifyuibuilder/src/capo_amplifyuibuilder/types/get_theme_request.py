"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.uuid


class GetThemeRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThemeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetThemeRequest:
    out: GetThemeRequest = {}  # type: ignore[typeddict-item]
    return out
