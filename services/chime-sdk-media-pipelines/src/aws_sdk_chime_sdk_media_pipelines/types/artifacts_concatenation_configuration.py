"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsConcatenationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration


class ArtifactsConcatenationConfiguration(TypedDict, closed=True):
    audio: "aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration.AudioConcatenationConfiguration"
    """<p>The configuration for the audio artifacts concatenation.</p>"""
    video: "aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration.VideoConcatenationConfiguration"
    """<p>The configuration for the video artifacts concatenation.</p>"""
    content: "aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration.ContentConcatenationConfiguration"
    """<p>The configuration for the content artifacts concatenation.</p>"""
    data_channel: "aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration.DataChannelConcatenationConfiguration"
    """<p>The configuration for the data channel artifacts concatenation.</p>"""
    transcription_messages: "aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration.TranscriptionMessagesConcatenationConfiguration"
    """<p>The configuration for the transcription messages artifacts concatenation.</p>"""
    meeting_events: "aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration.MeetingEventsConcatenationConfiguration"
    """<p>The configuration for the meeting events artifacts concatenation.</p>"""
    composited_video: "aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration.CompositedVideoConcatenationConfiguration"
    """<p>The configuration for the composited video artifacts concatenation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactsConcatenationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration

    out["Audio"] = (
        aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration.serialize_json(
            value["audio"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration

    out["Video"] = (
        aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration.serialize_json(
            value["video"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration

    out["Content"] = (
        aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration.serialize_json(
            value["content"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration

    out["DataChannel"] = (
        aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration.serialize_json(
            value["data_channel"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration

    out["TranscriptionMessages"] = (
        aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration.serialize_json(
            value["transcription_messages"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration

    out["MeetingEvents"] = (
        aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration.serialize_json(
            value["meeting_events"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration

    out["CompositedVideo"] = (
        aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration.serialize_json(
            value["composited_video"]
        )
    )
    return out


def deserialize_json(data: dict) -> ArtifactsConcatenationConfiguration:
    out: ArtifactsConcatenationConfiguration = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration

        out["audio"] = (
            aws_sdk_chime_sdk_media_pipelines.types.audio_concatenation_configuration.deserialize_json(
                data["Audio"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConcatenationConfiguration.audio required")
    if "Video" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration

        out["video"] = (
            aws_sdk_chime_sdk_media_pipelines.types.video_concatenation_configuration.deserialize_json(
                data["Video"]
            )
        )
    else:
        raise DeserializationError("ArtifactsConcatenationConfiguration.video required")
    if "Content" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration

        out["content"] = (
            aws_sdk_chime_sdk_media_pipelines.types.content_concatenation_configuration.deserialize_json(
                data["Content"]
            )
        )
    else:
        raise DeserializationError(
            "ArtifactsConcatenationConfiguration.content required"
        )
    if "DataChannel" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration

        out["data_channel"] = (
            aws_sdk_chime_sdk_media_pipelines.types.data_channel_concatenation_configuration.deserialize_json(
                data["DataChannel"]
            )
        )
    else:
        raise DeserializationError(
            "ArtifactsConcatenationConfiguration.data_channel required"
        )
    if "TranscriptionMessages" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration

        out["transcription_messages"] = (
            aws_sdk_chime_sdk_media_pipelines.types.transcription_messages_concatenation_configuration.deserialize_json(
                data["TranscriptionMessages"]
            )
        )
    else:
        raise DeserializationError(
            "ArtifactsConcatenationConfiguration.transcription_messages required"
        )
    if "MeetingEvents" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration

        out["meeting_events"] = (
            aws_sdk_chime_sdk_media_pipelines.types.meeting_events_concatenation_configuration.deserialize_json(
                data["MeetingEvents"]
            )
        )
    else:
        raise DeserializationError(
            "ArtifactsConcatenationConfiguration.meeting_events required"
        )
    if "CompositedVideo" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration

        out["composited_video"] = (
            aws_sdk_chime_sdk_media_pipelines.types.composited_video_concatenation_configuration.deserialize_json(
                data["CompositedVideo"]
            )
        )
    else:
        raise DeserializationError(
            "ArtifactsConcatenationConfiguration.composited_video required"
        )
    return out
