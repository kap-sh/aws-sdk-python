"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportFormsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ExportFormsRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app to export forms to.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFormsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportFormsRequest:
    out: ExportFormsRequest = {}  # type: ignore[typeddict-item]
    return out
