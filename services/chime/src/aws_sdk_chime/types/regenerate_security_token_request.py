"""Generated from Smithy shape ``com.amazonaws.chime#RegenerateSecurityTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class RegenerateSecurityTokenRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegenerateSecurityTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RegenerateSecurityTokenRequest:
    out: RegenerateSecurityTokenRequest = {}  # type: ignore[typeddict-item]
    return out
