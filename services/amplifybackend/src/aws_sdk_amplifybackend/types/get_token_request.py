"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class GetTokenRequest(TypedDict):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    session_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The session ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTokenRequest:
    out: GetTokenRequest = {}  # type: ignore[typeddict-item]
    return out
