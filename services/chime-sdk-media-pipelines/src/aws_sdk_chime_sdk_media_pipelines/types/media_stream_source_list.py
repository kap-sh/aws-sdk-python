"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_source

MediaStreamSourceList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_stream_source.MediaStreamSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSourceList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaStreamSourceList:
    import aws_sdk_chime_sdk_media_pipelines.types.media_stream_source

    out: MediaStreamSourceList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_stream_source.deserialize_json(
                item
            )
        )
    return out
