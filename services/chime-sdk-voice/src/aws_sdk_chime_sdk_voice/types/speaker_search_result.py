"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.confidence_score
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class SpeakerSearchResult(TypedDict, closed=True):
    confidence_score: "aws_sdk_chime_sdk_voice.types.confidence_score.ConfidenceScore"
    """<p>The confidence score in the speaker search analysis.</p>"""
    voice_profile_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The voice profile ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchResult) -> dict:
    out: dict = {}
    out["ConfidenceScore"] = value.get("confidence_score", 0)
    if "voice_profile_id" in value:
        out["VoiceProfileId"] = value["voice_profile_id"]
    return out


def deserialize_json(data: dict) -> SpeakerSearchResult:
    out: SpeakerSearchResult = {}  # type: ignore[typeddict-item]
    if "ConfidenceScore" in data:
        out["confidence_score"] = data["ConfidenceScore"]
    else:
        out["confidence_score"] = 0
    if "VoiceProfileId" in data:
        out["voice_profile_id"] = data["VoiceProfileId"]
    return out
