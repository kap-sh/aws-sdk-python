"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StartVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.client_request_id
    import capo_chime_sdk_voice.types.language_code
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.non_empty_string256


class StartVoiceToneAnalysisTaskRequest(TypedDict, closed=True):
    voice_connector_id: (
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    transaction_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    """<p>The transaction ID.</p>"""
    language_code: "capo_chime_sdk_voice.types.language_code.LanguageCode"
    """<p>The language code.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
    ]
    """<p>The unique identifier for the client request. Use a different token for different voice tone analysis tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    out["TransactionId"] = value["transaction_id"]
    import capo_chime_sdk_voice.types.language_code

    out["LanguageCode"] = capo_chime_sdk_voice.types.language_code.serialize_json(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartVoiceToneAnalysisTaskRequest:
    out: StartVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    else:
        raise DeserializationError(
            "StartVoiceToneAnalysisTaskRequest.transaction_id required"
        )
    if "LanguageCode" in data:
        import capo_chime_sdk_voice.types.language_code

        out["language_code"] = (
            capo_chime_sdk_voice.types.language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartVoiceToneAnalysisTaskRequest.language_code required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
