"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CallDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.non_empty_string256


class CallDetails(TypedDict, closed=True):
    voice_connector_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    ]
    """<p>The Voice Connector ID.</p>"""
    transaction_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The transaction ID of a Voice Connector call.</p>"""
    is_caller: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Identifies a person as the caller or the callee.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallDetails) -> dict:
    out: dict = {}
    if "voice_connector_id" in value:
        out["VoiceConnectorId"] = value["voice_connector_id"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "is_caller" in value:
        out["IsCaller"] = value["is_caller"]
    return out


def deserialize_json(data: dict) -> CallDetails:
    out: CallDetails = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorId" in data:
        out["voice_connector_id"] = data["VoiceConnectorId"]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    if "IsCaller" in data:
        out["is_caller"] = data["IsCaller"]
    return out
