"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration


class ArtifactsConfiguration(TypedDict):
    audio: "aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration.AudioArtifactsConfiguration"
    """<p>The configuration for the audio artifacts.</p>"""
    video: "aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration.VideoArtifactsConfiguration"
    """<p>The configuration for the video artifacts.</p>"""
    content: "aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration.ContentArtifactsConfiguration"
    """<p>The configuration for the content artifacts.</p>"""
    composited_video: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.CompositedVideoArtifactsConfiguration"
    ]
    """<p>Enables video compositing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration

    out["Audio"] = (
        aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration.serialize_json(
            value["audio"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration

    out["Video"] = (
        aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration.serialize_json(
            value["video"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration

    out["Content"] = (
        aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration.serialize_json(
            value["content"]
        )
    )
    if "composited_video" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["CompositedVideo"] = (
            aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.serialize_json(
                value["composited_video"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArtifactsConfiguration:
    out: ArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration

        out["audio"] = (
            aws_sdk_chime_sdk_media_pipelines.types.audio_artifacts_configuration.deserialize_json(
                data["Audio"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.audio required")
    if "Video" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration

        out["video"] = (
            aws_sdk_chime_sdk_media_pipelines.types.video_artifacts_configuration.deserialize_json(
                data["Video"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.video required")
    if "Content" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration

        out["content"] = (
            aws_sdk_chime_sdk_media_pipelines.types.content_artifacts_configuration.deserialize_json(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConfiguration.content required")
    if "CompositedVideo" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["composited_video"] = (
            aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.deserialize_json(
                data["CompositedVideo"]
            )
        )
    return out
