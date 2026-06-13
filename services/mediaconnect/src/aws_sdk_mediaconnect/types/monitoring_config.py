"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MonitoringConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting
    import aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting
    import aws_sdk_mediaconnect.types.content_quality_analysis_state
    import aws_sdk_mediaconnect.types.thumbnail_state


class MonitoringConfig(TypedDict):
    thumbnail_state: NotRequired[
        "aws_sdk_mediaconnect.types.thumbnail_state.ThumbnailState"
    ]
    """<p> Indicates whether thumbnails are enabled or disabled.</p>"""
    audio_monitoring_settings: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting.__listOfAudioMonitoringSetting"
    ]
    """<p> Contains the settings for audio stream metrics monitoring.</p>"""
    content_quality_analysis_state: NotRequired[
        "aws_sdk_mediaconnect.types.content_quality_analysis_state.ContentQualityAnalysisState"
    ]
    """<p> Indicates whether content quality analysis is enabled or disabled.</p>"""
    video_monitoring_settings: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting.__listOfVideoMonitoringSetting"
    ]
    """<p> Contains the settings for video stream metrics monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitoringConfig) -> dict:
    out: dict = {}
    if "thumbnail_state" in value:
        import aws_sdk_mediaconnect.types.thumbnail_state

        out["thumbnailState"] = (
            aws_sdk_mediaconnect.types.thumbnail_state.serialize_json(
                value["thumbnail_state"]
            )
        )
    if "audio_monitoring_settings" in value:
        import aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting

        out["audioMonitoringSettings"] = (
            aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting.serialize_json(
                value["audio_monitoring_settings"]
            )
        )
    if "content_quality_analysis_state" in value:
        import aws_sdk_mediaconnect.types.content_quality_analysis_state

        out["contentQualityAnalysisState"] = (
            aws_sdk_mediaconnect.types.content_quality_analysis_state.serialize_json(
                value["content_quality_analysis_state"]
            )
        )
    if "video_monitoring_settings" in value:
        import aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting

        out["videoMonitoringSettings"] = (
            aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting.serialize_json(
                value["video_monitoring_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitoringConfig:
    out: MonitoringConfig = {}  # type: ignore[typeddict-item]
    if "thumbnailState" in data:
        import aws_sdk_mediaconnect.types.thumbnail_state

        out["thumbnail_state"] = (
            aws_sdk_mediaconnect.types.thumbnail_state.deserialize_json(
                data["thumbnailState"]
            )
        )
    if "audioMonitoringSettings" in data:
        import aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting

        out["audio_monitoring_settings"] = (
            aws_sdk_mediaconnect.types.__list_of_audio_monitoring_setting.deserialize_json(
                data["audioMonitoringSettings"]
            )
        )
    if "contentQualityAnalysisState" in data:
        import aws_sdk_mediaconnect.types.content_quality_analysis_state

        out["content_quality_analysis_state"] = (
            aws_sdk_mediaconnect.types.content_quality_analysis_state.deserialize_json(
                data["contentQualityAnalysisState"]
            )
        )
    if "videoMonitoringSettings" in data:
        import aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting

        out["video_monitoring_settings"] = (
            aws_sdk_mediaconnect.types.__list_of_video_monitoring_setting.deserialize_json(
                data["videoMonitoringSettings"]
            )
        )
    return out
