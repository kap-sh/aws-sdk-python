"""Generated from Smithy shape ``com.amazonaws.chime#DeleteEventsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class DeleteEventsConfigurationRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventsConfigurationRequest:
    out: DeleteEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
