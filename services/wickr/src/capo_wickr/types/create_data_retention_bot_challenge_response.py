"""Generated from Smithy shape ``com.amazonaws.wickr#CreateDataRetentionBotChallengeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.sensitive_string


class CreateDataRetentionBotChallengeResponse(TypedDict, closed=True):
    challenge: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The newly generated challenge password for the data retention bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataRetentionBotChallengeResponse) -> dict:
    out: dict = {}
    out["challenge"] = value["challenge"]
    return out


def deserialize_json(data: dict) -> CreateDataRetentionBotChallengeResponse:
    out: CreateDataRetentionBotChallengeResponse = {}  # type: ignore[typeddict-item]
    if "challenge" in data:
        out["challenge"] = data["challenge"]
    else:
        raise DeserializationError(
            "CreateDataRetentionBotChallengeResponse.challenge required"
        )
    return out
