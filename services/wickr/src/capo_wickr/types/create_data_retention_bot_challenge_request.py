"""Generated from Smithy shape ``com.amazonaws.wickr#CreateDataRetentionBotChallengeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.network_id


class CreateDataRetentionBotChallengeRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the data retention bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataRetentionBotChallengeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateDataRetentionBotChallengeRequest:
    out: CreateDataRetentionBotChallengeRequest = {}  # type: ignore[typeddict-item]
    return out
