"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetVoiceTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.voice_template_response


class GetVoiceTemplateResponse(TypedDict):
    voice_template_response: NotRequired[
        "aws_sdk_pinpoint.types.voice_template_response.VoiceTemplateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceTemplateResponse) -> dict:
    out: dict = {}
    if "voice_template_response" in value:
        import aws_sdk_pinpoint.types.voice_template_response

        out["VoiceTemplateResponse"] = (
            aws_sdk_pinpoint.types.voice_template_response.serialize_json(
                value["voice_template_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceTemplateResponse:
    out: GetVoiceTemplateResponse = {}  # type: ignore[typeddict-item]
    if "VoiceTemplateResponse" in data:
        import aws_sdk_pinpoint.types.voice_template_response

        out["voice_template_response"] = (
            aws_sdk_pinpoint.types.voice_template_response.deserialize_json(
                data["VoiceTemplateResponse"]
            )
        )
    return out
