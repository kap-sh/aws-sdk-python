"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Playlists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.playlist

Playlists: TypeAlias = list["capo_elastic_transcoder.types.playlist.Playlist"]


# --- restJson1 ser/de ---
def serialize_json(value: Playlists) -> list:
    import capo_elastic_transcoder.types.playlist

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.playlist.serialize_json(item))
    return out


def deserialize_json(data: list) -> Playlists:
    import capo_elastic_transcoder.types.playlist

    out: Playlists = []
    for item in data:
        out.append(capo_elastic_transcoder.types.playlist.deserialize_json(item))
    return out
