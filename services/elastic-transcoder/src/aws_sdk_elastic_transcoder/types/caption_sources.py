"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CaptionSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.caption_source

CaptionSources: TypeAlias = list[
    "aws_sdk_elastic_transcoder.types.caption_source.CaptionSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSources) -> list:
    import aws_sdk_elastic_transcoder.types.caption_source

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.caption_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaptionSources:
    import aws_sdk_elastic_transcoder.types.caption_source

    out: CaptionSources = []
    for item in data:
        out.append(
            aws_sdk_elastic_transcoder.types.caption_source.deserialize_json(item)
        )
    return out
