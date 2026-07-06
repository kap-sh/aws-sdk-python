"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetMetadataRequest``."""

from typing_extensions import TypedDict


class GetMetadataRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMetadataRequest:
    out: GetMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
