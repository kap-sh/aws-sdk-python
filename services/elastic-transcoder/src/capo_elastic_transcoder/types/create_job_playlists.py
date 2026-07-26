"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreateJobPlaylists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.create_job_playlist

CreateJobPlaylists: TypeAlias = list[
    "capo_elastic_transcoder.types.create_job_playlist.CreateJobPlaylist"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobPlaylists) -> list:
    import capo_elastic_transcoder.types.create_job_playlist

    out: list = []
    for item in value:
        out.append(
            capo_elastic_transcoder.types.create_job_playlist.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateJobPlaylists:
    import capo_elastic_transcoder.types.create_job_playlist

    out: CreateJobPlaylists = []
    for item in data:
        out.append(
            capo_elastic_transcoder.types.create_job_playlist.deserialize_json(item)
        )
    return out
