"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimedMetadataInsertion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_id3_insertion


class TimedMetadataInsertion(TypedDict, closed=True):
    id3_insertions: NotRequired[
        "capo_mediaconvert.types.__list_of_id3_insertion.__listOfId3Insertion"
    ]
    """Id3Insertions contains the array of Id3Insertion instances."""


# --- restJson1 ser/de ---
def serialize_json(value: TimedMetadataInsertion) -> dict:
    out: dict = {}
    if "id3_insertions" in value:
        import capo_mediaconvert.types.__list_of_id3_insertion

        out["id3Insertions"] = (
            capo_mediaconvert.types.__list_of_id3_insertion.serialize_json(
                value["id3_insertions"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimedMetadataInsertion:
    out: TimedMetadataInsertion = {}  # type: ignore[typeddict-item]
    if "id3Insertions" in data:
        import capo_mediaconvert.types.__list_of_id3_insertion

        out["id3_insertions"] = (
            capo_mediaconvert.types.__list_of_id3_insertion.deserialize_json(
                data["id3Insertions"]
            )
        )
    return out
