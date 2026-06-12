"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Artworks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.artwork

Artworks: TypeAlias = list["aws_sdk_elastic_transcoder.types.artwork.Artwork"]


# --- restJson1 ser/de ---
def serialize_json(value: Artworks) -> list:
    import aws_sdk_elastic_transcoder.types.artwork

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.artwork.serialize_json(item))
    return out


def deserialize_json(data: list) -> Artworks:
    import aws_sdk_elastic_transcoder.types.artwork

    out: Artworks = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.artwork.deserialize_json(item))
    return out
