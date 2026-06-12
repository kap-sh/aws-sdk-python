"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeleteTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class DeleteTokenRequest(TypedDict):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    session_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The session ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTokenRequest:
    out: DeleteTokenRequest = {}  # type: ignore[typeddict-item]
    return out
