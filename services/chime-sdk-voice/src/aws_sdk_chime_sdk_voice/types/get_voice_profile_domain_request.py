"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceProfileDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class GetVoiceProfileDomainRequest(TypedDict, closed=True):
    voice_profile_domain_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The voice profile domain ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceProfileDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceProfileDomainRequest:
    out: GetVoiceProfileDomainRequest = {}  # type: ignore[typeddict-item]
    return out
