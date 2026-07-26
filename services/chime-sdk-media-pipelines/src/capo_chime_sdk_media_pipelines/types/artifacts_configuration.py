"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration
    import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration
    import capo_chime_sdk_media_pipelines.types.content_artifacts_configuration
    import capo_chime_sdk_media_pipelines.types.video_artifacts_configuration


class ArtifactsConfiguration(TypedDict, closed=True):
    audio: "capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration.AudioArtifactsConfiguration"
    """<p>The configuration for the audio artifacts.</p>"""
    video: "capo_chime_sdk_media_pipelines.types.video_artifacts_configuration.VideoArtifactsConfiguration"
    """<p>The configuration for the video artifacts.</p>"""
    content: "capo_chime_sdk_media_pipelines.types.content_artifacts_configuration.ContentArtifactsConfiguration"
    """<p>The configuration for the content artifacts.</p>"""
    composited_video: NotRequired[
        "capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.CompositedVideoArtifactsConfiguration"
    ]
    """<p>Enables video compositing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactsConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration

    out["Audio"] = (
        capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration.serialize_json(
            value["audio"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.video_artifacts_configuration

    out["Video"] = (
        capo_chime_sdk_media_pipelines.types.video_artifacts_configuration.serialize_json(
            value["video"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.content_artifacts_configuration

    out["Content"] = (
        capo_chime_sdk_media_pipelines.types.content_artifacts_configuration.serialize_json(
            value["content"]
        )
    )
    if "composited_video" in value:
        import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["CompositedVideo"] = (
            capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.serialize_json(
                value["composited_video"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArtifactsConfiguration:
    out: ArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration

        out["audio"] = (
            capo_chime_sdk_media_pipelines.types.audio_artifacts_configuration.deserialize_json(
                data["Audio"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.audio required")
    if "Video" in data:
        import capo_chime_sdk_media_pipelines.types.video_artifacts_configuration

        out["video"] = (
            capo_chime_sdk_media_pipelines.types.video_artifacts_configuration.deserialize_json(
                data["Video"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.video required")
    if "Content" in data:
        import capo_chime_sdk_media_pipelines.types.content_artifacts_configuration

        out["content"] = (
            capo_chime_sdk_media_pipelines.types.content_artifacts_configuration.deserialize_json(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.content required")
    if "CompositedVideo" in data:
        import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["composited_video"] = (
            capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.deserialize_json(
                data["CompositedVideo"]
            )
        )
    return out
