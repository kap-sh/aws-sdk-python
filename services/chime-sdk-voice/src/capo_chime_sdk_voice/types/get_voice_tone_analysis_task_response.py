"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceToneAnalysisTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_tone_analysis_task


class GetVoiceToneAnalysisTaskResponse(TypedDict, closed=True):
    voice_tone_analysis_task: NotRequired[
        "capo_chime_sdk_voice.types.voice_tone_analysis_task.VoiceToneAnalysisTask"
    ]
    """<p>The details of the voice tone analysis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceToneAnalysisTaskResponse) -> dict:
    out: dict = {}
    if "voice_tone_analysis_task" in value:
        import capo_chime_sdk_voice.types.voice_tone_analysis_task

        out["VoiceToneAnalysisTask"] = (
            capo_chime_sdk_voice.types.voice_tone_analysis_task.serialize_json(
                value["voice_tone_analysis_task"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceToneAnalysisTaskResponse:
    out: GetVoiceToneAnalysisTaskResponse = {}  # type: ignore[typeddict-item]
    if "VoiceToneAnalysisTask" in data:
        import capo_chime_sdk_voice.types.voice_tone_analysis_task

        out["voice_tone_analysis_task"] = (
            capo_chime_sdk_voice.types.voice_tone_analysis_task.deserialize_json(
                data["VoiceToneAnalysisTask"]
            )
        )
    return out
