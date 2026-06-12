"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Playlists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.playlist

Playlists: TypeAlias = list["aws_sdk_elastic_transcoder.types.playlist.Playlist"]


# --- restJson1 ser/de ---
def serialize_json(value: Playlists) -> list:
    import aws_sdk_elastic_transcoder.types.playlist

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.playlist.serialize_json(item))
    return out


def deserialize_json(data: list) -> Playlists:
    import aws_sdk_elastic_transcoder.types.playlist

    out: Playlists = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.playlist.deserialize_json(item))
    return out
