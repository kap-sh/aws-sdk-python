"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceProfileDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class DeleteVoiceProfileDomainRequest(TypedDict):
    voice_profile_domain_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The voice profile domain ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceProfileDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceProfileDomainRequest:
    out: DeleteVoiceProfileDomainRequest = {}  # type: ignore[typeddict-item]
    return out
