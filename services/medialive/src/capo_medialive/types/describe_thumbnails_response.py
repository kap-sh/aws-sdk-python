"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeThumbnailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_thumbnail_detail


class DescribeThumbnailsResponse(TypedDict, closed=True):
    thumbnail_details: NotRequired[
        "capo_medialive.types.__list_of_thumbnail_detail.__listOfThumbnailDetail"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThumbnailsResponse) -> dict:
    out: dict = {}
    if "thumbnail_details" in value:
        import capo_medialive.types.__list_of_thumbnail_detail

        out["thumbnailDetails"] = (
            capo_medialive.types.__list_of_thumbnail_detail.serialize_json(
                value["thumbnail_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeThumbnailsResponse:
    out: DescribeThumbnailsResponse = {}  # type: ignore[typeddict-item]
    if "thumbnailDetails" in data:
        import capo_medialive.types.__list_of_thumbnail_detail

        out["thumbnail_details"] = (
            capo_medialive.types.__list_of_thumbnail_detail.deserialize_json(
                data["thumbnailDetails"]
            )
        )
    return out
