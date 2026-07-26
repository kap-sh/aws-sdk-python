"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.speaker_search_result_list


class SpeakerSearchDetails(TypedDict, closed=True):
    results: NotRequired[
        "capo_chime_sdk_voice.types.speaker_search_result_list.SpeakerSearchResultList"
    ]
    """<p>The result value in the speaker search details.</p>"""
    voiceprint_generation_status: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The status of a voice print generation operation, <code>VoiceprintGenerationSuccess</code> or <code>VoiceprintGenerationFailure</code>..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchDetails) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_chime_sdk_voice.types.speaker_search_result_list

        out["Results"] = (
            capo_chime_sdk_voice.types.speaker_search_result_list.serialize_json(
                value["results"]
            )
        )
    if "voiceprint_generation_status" in value:
        out["VoiceprintGenerationStatus"] = value["voiceprint_generation_status"]
    return out


def deserialize_json(data: dict) -> SpeakerSearchDetails:
    out: SpeakerSearchDetails = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_chime_sdk_voice.types.speaker_search_result_list

        out["results"] = (
            capo_chime_sdk_voice.types.speaker_search_result_list.deserialize_json(
                data["Results"]
            )
        )
    if "VoiceprintGenerationStatus" in data:
        out["voiceprint_generation_status"] = data["VoiceprintGenerationStatus"]
    return out
