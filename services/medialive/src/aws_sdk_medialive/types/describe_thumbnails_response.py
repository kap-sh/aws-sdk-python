"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeThumbnailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_thumbnail_detail


class DescribeThumbnailsResponse(TypedDict):
    thumbnail_details: NotRequired[
        "aws_sdk_medialive.types.__list_of_thumbnail_detail.__listOfThumbnailDetail"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThumbnailsResponse) -> dict:
    out: dict = {}
    if "thumbnail_details" in value:
        import aws_sdk_medialive.types.__list_of_thumbnail_detail

        out["thumbnailDetails"] = (
            aws_sdk_medialive.types.__list_of_thumbnail_detail.serialize_json(
                value["thumbnail_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeThumbnailsResponse:
    out: DescribeThumbnailsResponse = {}  # type: ignore[typeddict-item]
    if "thumbnailDetails" in data:
        import aws_sdk_medialive.types.__list_of_thumbnail_detail

        out["thumbnail_details"] = (
            aws_sdk_medialive.types.__list_of_thumbnail_detail.deserialize_json(
                data["thumbnailDetails"]
            )
        )
    return out
