"""Generated from Smithy shape ``com.amazonaws.chime#GetEventsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class GetEventsConfigurationRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventsConfigurationRequest:
    out: GetEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
