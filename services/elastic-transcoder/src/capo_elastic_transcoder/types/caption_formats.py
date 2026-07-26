"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CaptionFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.caption_format

CaptionFormats: TypeAlias = list[
    "capo_elastic_transcoder.types.caption_format.CaptionFormat"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionFormats) -> list:
    import capo_elastic_transcoder.types.caption_format

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.caption_format.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaptionFormats:
    import capo_elastic_transcoder.types.caption_format

    out: CaptionFormats = []
    for item in data:
        out.append(capo_elastic_transcoder.types.caption_format.deserialize_json(item))
    return out
