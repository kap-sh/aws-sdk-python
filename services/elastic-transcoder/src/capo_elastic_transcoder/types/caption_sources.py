"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CaptionSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.caption_source

CaptionSources: TypeAlias = list[
    "capo_elastic_transcoder.types.caption_source.CaptionSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSources) -> list:
    import capo_elastic_transcoder.types.caption_source

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.caption_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaptionSources:
    import capo_elastic_transcoder.types.caption_source

    out: CaptionSources = []
    for item in data:
        out.append(capo_elastic_transcoder.types.caption_source.deserialize_json(item))
    return out
