"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceAnalyticsProcessorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status


class VoiceAnalyticsProcessorConfiguration(TypedDict):
    speaker_search_status: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.VoiceAnalyticsConfigurationStatus"
    ]
    """<p>The status of the speaker search task.</p>"""
    voice_tone_analysis_status: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.VoiceAnalyticsConfigurationStatus"
    ]
    """<p>The status of the voice tone analysis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceAnalyticsProcessorConfiguration) -> dict:
    out: dict = {}
    if "speaker_search_status" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status

        out["SpeakerSearchStatus"] = (
            aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.serialize_json(
                value["speaker_search_status"]
            )
        )
    if "voice_tone_analysis_status" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status

        out["VoiceToneAnalysisStatus"] = (
            aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.serialize_json(
                value["voice_tone_analysis_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceAnalyticsProcessorConfiguration:
    out: VoiceAnalyticsProcessorConfiguration = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchStatus" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status

        out["speaker_search_status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.deserialize_json(
                data["SpeakerSearchStatus"]
            )
        )
    if "VoiceToneAnalysisStatus" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status

        out["voice_tone_analysis_status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.voice_analytics_configuration_status.deserialize_json(
                data["VoiceToneAnalysisStatus"]
            )
        )
    return out
