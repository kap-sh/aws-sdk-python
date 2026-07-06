"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorOriginationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.origination


class PutVoiceConnectorOriginationResponse(TypedDict, closed=True):
    origination: NotRequired["aws_sdk_chime_sdk_voice.types.origination.Origination"]
    """<p>The updated origination settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorOriginationResponse) -> dict:
    out: dict = {}
    if "origination" in value:
        import aws_sdk_chime_sdk_voice.types.origination

        out["Origination"] = aws_sdk_chime_sdk_voice.types.origination.serialize_json(
            value["origination"]
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorOriginationResponse:
    out: PutVoiceConnectorOriginationResponse = {}  # type: ignore[typeddict-item]
    if "Origination" in data:
        import aws_sdk_chime_sdk_voice.types.origination

        out["origination"] = aws_sdk_chime_sdk_voice.types.origination.deserialize_json(
            data["Origination"]
        )
    return out
