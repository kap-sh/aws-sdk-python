"""Generated from Smithy shape ``com.amazonaws.chime#GetBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class GetBotRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotRequest:
    out: GetBotRequest = {}  # type: ignore[typeddict-item]
    return out
