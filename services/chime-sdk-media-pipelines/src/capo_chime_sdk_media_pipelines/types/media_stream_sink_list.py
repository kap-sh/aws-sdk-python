"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

MediaStreamSinkList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_stream_sink.MediaStreamSink"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSinkList) -> list:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_sink.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MediaStreamSinkList:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

    out: MediaStreamSinkList = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_sink.deserialize_json(
                item
            )
        )
    return out
