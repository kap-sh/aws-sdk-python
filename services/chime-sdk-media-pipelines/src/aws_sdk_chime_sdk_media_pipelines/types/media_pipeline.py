"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline
    import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline
    import aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline


class MediaPipeline(TypedDict, closed=True):
    media_capture_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.MediaCapturePipeline"
    ]
    """<p>A pipeline that enables users to capture audio and video.</p>"""
    media_live_connector_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline.MediaLiveConnectorPipeline"
    ]
    """<p>The connector pipeline of the media pipeline.</p>"""
    media_concatenation_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.MediaConcatenationPipeline"
    ]
    """<p>The media concatenation pipeline in a media pipeline.</p>"""
    media_insights_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline.MediaInsightsPipeline"
    ]
    """<p>The media insights pipeline of a media pipeline.</p>"""
    media_stream_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline.MediaStreamPipeline"
    ]
    """<p>Designates a media pipeline as a media stream pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipeline) -> dict:
    out: dict = {}
    if "media_capture_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["MediaCapturePipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.serialize_json(
                value["media_capture_pipeline"]
            )
        )
    if "media_live_connector_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["MediaLiveConnectorPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline.serialize_json(
                value["media_live_connector_pipeline"]
            )
        )
    if "media_concatenation_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["MediaConcatenationPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.serialize_json(
                value["media_concatenation_pipeline"]
            )
        )
    if "media_insights_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["MediaInsightsPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline.serialize_json(
                value["media_insights_pipeline"]
            )
        )
    if "media_stream_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["MediaStreamPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline.serialize_json(
                value["media_stream_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPipeline:
    out: MediaPipeline = {}  # type: ignore[typeddict-item]
    if "MediaCapturePipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.deserialize_json(
                data["MediaCapturePipeline"]
            )
        )
    if "MediaLiveConnectorPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["media_live_connector_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_live_connector_pipeline.deserialize_json(
                data["MediaLiveConnectorPipeline"]
            )
        )
    if "MediaConcatenationPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.deserialize_json(
                data["MediaConcatenationPipeline"]
            )
        )
    if "MediaInsightsPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["media_insights_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline.deserialize_json(
                data["MediaInsightsPipeline"]
            )
        )
    if "MediaStreamPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["media_stream_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline.deserialize_json(
                data["MediaStreamPipeline"]
            )
        )
    return out
