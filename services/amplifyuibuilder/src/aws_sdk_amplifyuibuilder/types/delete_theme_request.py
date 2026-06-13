"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#DeleteThemeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.uuid


class DeleteThemeRequest(TypedDict):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the theme to delete.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the theme to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThemeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThemeRequest:
    out: DeleteThemeRequest = {}  # type: ignore[typeddict-item]
    return out
