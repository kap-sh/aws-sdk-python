"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorTerminationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.termination


class GetVoiceConnectorTerminationResponse(TypedDict):
    termination: NotRequired["aws_sdk_chime_sdk_voice.types.termination.Termination"]
    """<p>The termination setting details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorTerminationResponse) -> dict:
    out: dict = {}
    if "termination" in value:
        import aws_sdk_chime_sdk_voice.types.termination

        out["Termination"] = aws_sdk_chime_sdk_voice.types.termination.serialize_json(
            value["termination"]
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorTerminationResponse:
    out: GetVoiceConnectorTerminationResponse = {}  # type: ignore[typeddict-item]
    if "Termination" in data:
        import aws_sdk_chime_sdk_voice.types.termination

        out["termination"] = aws_sdk_chime_sdk_voice.types.termination.deserialize_json(
            data["Termination"]
        )
    return out
