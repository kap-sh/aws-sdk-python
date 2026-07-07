"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSink``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_type
    import aws_sdk_chime_sdk_media_pipelines.types.reserved_stream_capacity


class MediaStreamSink(TypedDict, closed=True):
    sink_arn: "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the Kinesis Video Stream pool returned by the <a>CreateMediaPipelineKinesisVideoStreamPool</a> API.</p>"""
    sink_type: "aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.MediaStreamPipelineSinkType"
    """<p>The media stream sink's type.</p>"""
    reserved_stream_capacity: "aws_sdk_chime_sdk_media_pipelines.types.reserved_stream_capacity.ReservedStreamCapacity"
    """<p>Specifies the number of streams that the sink can accept.</p>"""
    media_stream_type: (
        "aws_sdk_chime_sdk_media_pipelines.types.media_stream_type.MediaStreamType"
    )
    """<p>The media stream sink's media stream type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSink) -> dict:
    out: dict = {}
    out["SinkArn"] = value["sink_arn"]
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type

    out["SinkType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.serialize_json(
            value["sink_type"]
        )
    )
    out["ReservedStreamCapacity"] = value["reserved_stream_capacity"]
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_type

    out["MediaStreamType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.media_stream_type.serialize_json(
            value["media_stream_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaStreamSink:
    out: MediaStreamSink = {}  # type: ignore[typeddict-item]
    if "SinkArn" in data:
        out["sink_arn"] = data["SinkArn"]
    else:
        raise DeserializationError("MediaStreamSink.sink_arn required")
    if "SinkType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type

        out["sink_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_pipeline_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    else:
        raise DeserializationError("MediaStreamSink.sink_type required")
    if "ReservedStreamCapacity" in data:
        out["reserved_stream_capacity"] = data["ReservedStreamCapacity"]
    else:
        raise DeserializationError("MediaStreamSink.reserved_stream_capacity required")
    if "MediaStreamType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_stream_type

        out["media_stream_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_type.deserialize_json(
                data["MediaStreamType"]
            )
        )
    else:
        raise DeserializationError("MediaStreamSink.media_stream_type required")
    return out
