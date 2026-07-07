"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportComponentsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ExportComponentsRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app to export components to.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportComponentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportComponentsRequest:
    out: ExportComponentsRequest = {}  # type: ignore[typeddict-item]
    return out
