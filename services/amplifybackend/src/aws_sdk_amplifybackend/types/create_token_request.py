"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class CreateTokenRequest(TypedDict):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateTokenRequest:
    out: CreateTokenRequest = {}  # type: ignore[typeddict-item]
    return out
