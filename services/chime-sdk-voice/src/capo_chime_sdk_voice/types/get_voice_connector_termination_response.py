"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorTerminationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.termination


class GetVoiceConnectorTerminationResponse(TypedDict, closed=True):
    termination: NotRequired["capo_chime_sdk_voice.types.termination.Termination"]
    """<p>The termination setting details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorTerminationResponse) -> dict:
    out: dict = {}
    if "termination" in value:
        import capo_chime_sdk_voice.types.termination

        out["Termination"] = capo_chime_sdk_voice.types.termination.serialize_json(
            value["termination"]
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorTerminationResponse:
    out: GetVoiceConnectorTerminationResponse = {}  # type: ignore[typeddict-item]
    if "Termination" in data:
        import capo_chime_sdk_voice.types.termination

        out["termination"] = capo_chime_sdk_voice.types.termination.deserialize_json(
            data["Termination"]
        )
    return out
