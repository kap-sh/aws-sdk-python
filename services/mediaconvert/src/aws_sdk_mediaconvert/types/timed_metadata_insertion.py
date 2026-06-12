"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimedMetadataInsertion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_id3_insertion


class TimedMetadataInsertion(TypedDict):
    id3_insertions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_id3_insertion.__listOfId3Insertion"
    ]
    """Id3Insertions contains the array of Id3Insertion instances."""


# --- restJson1 ser/de ---
def serialize_json(value: TimedMetadataInsertion) -> dict:
    out: dict = {}
    if "id3_insertions" in value:
        import aws_sdk_mediaconvert.types.__list_of_id3_insertion

        out["id3Insertions"] = (
            aws_sdk_mediaconvert.types.__list_of_id3_insertion.serialize_json(
                value["id3_insertions"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimedMetadataInsertion:
    out: TimedMetadataInsertion = {}  # type: ignore[typeddict-item]
    if "id3Insertions" in data:
        import aws_sdk_mediaconvert.types.__list_of_id3_insertion

        out["id3_insertions"] = (
            aws_sdk_mediaconvert.types.__list_of_id3_insertion.deserialize_json(
                data["id3Insertions"]
            )
        )
    return out
