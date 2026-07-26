"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobAlbumArt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.artworks
    import capo_elastic_transcoder.types.merge_policy


class JobAlbumArt(TypedDict, closed=True):
    merge_policy: NotRequired["capo_elastic_transcoder.types.merge_policy.MergePolicy"]
    """<p>A policy that determines how Elastic Transcoder handles the existence of multiple album artwork files.</p> <ul> <li> <p> <code>Replace:</code> The specified album art replaces any existing album art.</p> </li> <li> <p> <code>Prepend:</code> The specified album art is placed in front of any existing album art.</p> </li> <li> <p> <code>Append:</code> The specified album art is placed after any existing album art.</p> </li> <li> <p> <code>Fallback:</code> If the original input file contains artwork, Elastic Transcoder uses that artwork for the output. If the original input does not contain artwork, Elastic Transcoder uses the specified album art file.</p> </li> </ul>"""
    artwork: NotRequired["capo_elastic_transcoder.types.artworks.Artworks"]
    """<p>The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20. Valid formats are <code>.jpg</code> and <code>.png</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobAlbumArt) -> dict:
    out: dict = {}
    if "merge_policy" in value:
        out["MergePolicy"] = value["merge_policy"]
    if "artwork" in value:
        import capo_elastic_transcoder.types.artworks

        out["Artwork"] = capo_elastic_transcoder.types.artworks.serialize_json(
            value["artwork"]
        )
    return out


def deserialize_json(data: dict) -> JobAlbumArt:
    out: JobAlbumArt = {}  # type: ignore[typeddict-item]
    if "MergePolicy" in data:
        out["merge_policy"] = data["MergePolicy"]
    if "Artwork" in data:
        import capo_elastic_transcoder.types.artworks

        out["artwork"] = capo_elastic_transcoder.types.artworks.deserialize_json(
            data["Artwork"]
        )
    return out
