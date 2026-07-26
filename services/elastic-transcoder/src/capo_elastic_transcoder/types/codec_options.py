"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CodecOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.codec_option

CodecOptions: TypeAlias = dict[
    "capo_elastic_transcoder.types.codec_option.CodecOption",
    "capo_elastic_transcoder.types.codec_option.CodecOption",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CodecOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CodecOptions:
    out: CodecOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
