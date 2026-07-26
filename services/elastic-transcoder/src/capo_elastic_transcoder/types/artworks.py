"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Artworks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.artwork

Artworks: TypeAlias = list["capo_elastic_transcoder.types.artwork.Artwork"]


# --- restJson1 ser/de ---
def serialize_json(value: Artworks) -> list:
    import capo_elastic_transcoder.types.artwork

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.artwork.serialize_json(item))
    return out


def deserialize_json(data: list) -> Artworks:
    import capo_elastic_transcoder.types.artwork

    out: Artworks = []
    for item in data:
        out.append(capo_elastic_transcoder.types.artwork.deserialize_json(item))
    return out
