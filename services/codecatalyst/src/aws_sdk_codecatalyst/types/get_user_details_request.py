"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetUserDetailsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetUserDetailsRequest(TypedDict):
    id: NotRequired["str"]
    """<p>The system-generated unique ID of the user. </p>"""
    user_name: NotRequired["str"]
    """<p>The name of the user as displayed in Amazon CodeCatalyst.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserDetailsRequest:
    out: GetUserDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
