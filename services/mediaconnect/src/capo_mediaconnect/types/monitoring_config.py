"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MonitoringConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_audio_monitoring_setting
    import capo_mediaconnect.types.__list_of_video_monitoring_setting
    import capo_mediaconnect.types.content_quality_analysis_state
    import capo_mediaconnect.types.thumbnail_state


class MonitoringConfig(TypedDict, closed=True):
    thumbnail_state: NotRequired[
        "capo_mediaconnect.types.thumbnail_state.ThumbnailState"
    ]
    """<p> Indicates whether thumbnails are enabled or disabled.</p>"""
    audio_monitoring_settings: NotRequired[
        "capo_mediaconnect.types.__list_of_audio_monitoring_setting.__listOfAudioMonitoringSetting"
    ]
    """<p> Contains the settings for audio stream metrics monitoring.</p>"""
    content_quality_analysis_state: NotRequired[
        "capo_mediaconnect.types.content_quality_analysis_state.ContentQualityAnalysisState"
    ]
    """<p> Indicates whether content quality analysis is enabled or disabled.</p>"""
    video_monitoring_settings: NotRequired[
        "capo_mediaconnect.types.__list_of_video_monitoring_setting.__listOfVideoMonitoringSetting"
    ]
    """<p> Contains the settings for video stream metrics monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitoringConfig) -> dict:
    out: dict = {}
    if "thumbnail_state" in value:
        import capo_mediaconnect.types.thumbnail_state

        out["thumbnailState"] = capo_mediaconnect.types.thumbnail_state.serialize_json(
            value["thumbnail_state"]
        )
    if "audio_monitoring_settings" in value:
        import capo_mediaconnect.types.__list_of_audio_monitoring_setting

        out["audioMonitoringSettings"] = (
            capo_mediaconnect.types.__list_of_audio_monitoring_setting.serialize_json(
                value["audio_monitoring_settings"]
            )
        )
    if "content_quality_analysis_state" in value:
        import capo_mediaconnect.types.content_quality_analysis_state

        out["contentQualityAnalysisState"] = (
            capo_mediaconnect.types.content_quality_analysis_state.serialize_json(
                value["content_quality_analysis_state"]
            )
        )
    if "video_monitoring_settings" in value:
        import capo_mediaconnect.types.__list_of_video_monitoring_setting

        out["videoMonitoringSettings"] = (
            capo_mediaconnect.types.__list_of_video_monitoring_setting.serialize_json(
                value["video_monitoring_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitoringConfig:
    out: MonitoringConfig = {}  # type: ignore[typeddict-item]
    if "thumbnailState" in data:
        import capo_mediaconnect.types.thumbnail_state

        out["thumbnail_state"] = (
            capo_mediaconnect.types.thumbnail_state.deserialize_json(
                data["thumbnailState"]
            )
        )
    if "audioMonitoringSettings" in data:
        import capo_mediaconnect.types.__list_of_audio_monitoring_setting

        out["audio_monitoring_settings"] = (
            capo_mediaconnect.types.__list_of_audio_monitoring_setting.deserialize_json(
                data["audioMonitoringSettings"]
            )
        )
    if "contentQualityAnalysisState" in data:
        import capo_mediaconnect.types.content_quality_analysis_state

        out["content_quality_analysis_state"] = (
            capo_mediaconnect.types.content_quality_analysis_state.deserialize_json(
                data["contentQualityAnalysisState"]
            )
        )
    if "videoMonitoringSettings" in data:
        import capo_mediaconnect.types.__list_of_video_monitoring_setting

        out["video_monitoring_settings"] = (
            capo_mediaconnect.types.__list_of_video_monitoring_setting.deserialize_json(
                data["videoMonitoringSettings"]
            )
        )
    return out
