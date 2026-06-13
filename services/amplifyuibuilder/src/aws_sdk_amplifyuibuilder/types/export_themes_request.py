"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportThemesRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ExportThemesRequest(TypedDict):
    app_id: "str"
    """<p>The unique ID of the Amplify app to export the themes to.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportThemesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportThemesRequest:
    out: ExportThemesRequest = {}  # type: ignore[typeddict-item]
    return out
