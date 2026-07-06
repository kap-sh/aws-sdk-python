"""Generated from Smithy shape ``com.amazonaws.chime#GetUserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.string


class GetUserSettingsRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "aws_sdk_chime.types.string.String"
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserSettingsRequest:
    out: GetUserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
