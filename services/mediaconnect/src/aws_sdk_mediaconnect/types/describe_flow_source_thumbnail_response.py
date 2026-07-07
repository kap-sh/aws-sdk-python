"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowSourceThumbnailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.thumbnail_details


class DescribeFlowSourceThumbnailResponse(TypedDict, closed=True):
    thumbnail_details: NotRequired[
        "aws_sdk_mediaconnect.types.thumbnail_details.ThumbnailDetails"
    ]
    """<p>The details of the thumbnail, including thumbnail base64 string, timecode and the time when thumbnail was generated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowSourceThumbnailResponse) -> dict:
    out: dict = {}
    if "thumbnail_details" in value:
        import aws_sdk_mediaconnect.types.thumbnail_details

        out["thumbnailDetails"] = (
            aws_sdk_mediaconnect.types.thumbnail_details.serialize_json(
                value["thumbnail_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeFlowSourceThumbnailResponse:
    out: DescribeFlowSourceThumbnailResponse = {}  # type: ignore[typeddict-item]
    if "thumbnailDetails" in data:
        import aws_sdk_mediaconnect.types.thumbnail_details

        out["thumbnail_details"] = (
            aws_sdk_mediaconnect.types.thumbnail_details.deserialize_json(
                data["thumbnailDetails"]
            )
        )
    return out
