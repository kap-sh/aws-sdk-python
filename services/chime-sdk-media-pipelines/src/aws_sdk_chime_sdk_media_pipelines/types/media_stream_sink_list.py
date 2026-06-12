"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink

MediaStreamSinkList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink.MediaStreamSink"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSinkList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaStreamSinkList:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink

    out: MediaStreamSinkList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_sink.deserialize_json(
                item
            )
        )
    return out
