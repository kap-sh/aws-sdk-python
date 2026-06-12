"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string256
    import aws_sdk_chime_sdk_voice.types.speaker_search_result_list


class SpeakerSearchDetails(TypedDict):
    results: NotRequired[
        "aws_sdk_chime_sdk_voice.types.speaker_search_result_list.SpeakerSearchResultList"
    ]
    """<p>The result value in the speaker search details.</p>"""
    voiceprint_generation_status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The status of a voice print generation operation, <code>VoiceprintGenerationSuccess</code> or <code>VoiceprintGenerationFailure</code>..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchDetails) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_chime_sdk_voice.types.speaker_search_result_list

        out["Results"] = (
            aws_sdk_chime_sdk_voice.types.speaker_search_result_list.serialize_json(
                value["results"]
            )
        )
    if "voiceprint_generation_status" in value:
        out["VoiceprintGenerationStatus"] = value["voiceprint_generation_status"]
    return out


def deserialize_json(data: dict) -> SpeakerSearchDetails:
    out: SpeakerSearchDetails = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_chime_sdk_voice.types.speaker_search_result_list

        out["results"] = (
            aws_sdk_chime_sdk_voice.types.speaker_search_result_list.deserialize_json(
                data["Results"]
            )
        )
    if "VoiceprintGenerationStatus" in data:
        out["voiceprint_generation_status"] = data["VoiceprintGenerationStatus"]
    return out
