"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateVoiceTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.voice_template_request


class CreateVoiceTemplateRequest(TypedDict, closed=True):
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""
    voice_template_request: NotRequired[
        "capo_pinpoint.types.voice_template_request.VoiceTemplateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceTemplateRequest) -> dict:
    out: dict = {}
    if "voice_template_request" in value:
        import capo_pinpoint.types.voice_template_request

        out["VoiceTemplateRequest"] = (
            capo_pinpoint.types.voice_template_request.serialize_json(
                value["voice_template_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceTemplateRequest:
    out: CreateVoiceTemplateRequest = {}  # type: ignore[typeddict-item]
    if "VoiceTemplateRequest" in data:
        import capo_pinpoint.types.voice_template_request

        out["voice_template_request"] = (
            capo_pinpoint.types.voice_template_request.deserialize_json(
                data["VoiceTemplateRequest"]
            )
        )
    return out
