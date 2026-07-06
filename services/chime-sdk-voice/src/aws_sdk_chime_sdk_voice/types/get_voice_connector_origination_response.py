"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorOriginationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.origination


class GetVoiceConnectorOriginationResponse(TypedDict, closed=True):
    origination: NotRequired["aws_sdk_chime_sdk_voice.types.origination.Origination"]
    """<p>The origination setting details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorOriginationResponse) -> dict:
    out: dict = {}
    if "origination" in value:
        import aws_sdk_chime_sdk_voice.types.origination

        out["Origination"] = aws_sdk_chime_sdk_voice.types.origination.serialize_json(
            value["origination"]
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorOriginationResponse:
    out: GetVoiceConnectorOriginationResponse = {}  # type: ignore[typeddict-item]
    if "Origination" in data:
        import aws_sdk_chime_sdk_voice.types.origination

        out["origination"] = aws_sdk_chime_sdk_voice.types.origination.deserialize_json(
            data["Origination"]
        )
    return out
