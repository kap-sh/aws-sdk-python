"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink

ConcatenationSinkList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink.ConcatenationSink"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSinkList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConcatenationSinkList:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink

    out: ConcatenationSinkList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.concatenation_sink.deserialize_json(
                item
            )
        )
    return out
