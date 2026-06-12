"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_thumbnail
    import aws_sdk_medialive.types.__string


class ThumbnailDetail(TypedDict):
    pipeline_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Pipeline ID"""
    thumbnails: NotRequired[
        "aws_sdk_medialive.types.__list_of_thumbnail.__listOfThumbnail"
    ]
    """thumbnails of a single pipeline"""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailDetail) -> dict:
    out: dict = {}
    if "pipeline_id" in value:
        out["pipelineId"] = value["pipeline_id"]
    if "thumbnails" in value:
        import aws_sdk_medialive.types.__list_of_thumbnail

        out["thumbnails"] = aws_sdk_medialive.types.__list_of_thumbnail.serialize_json(
            value["thumbnails"]
        )
    return out


def deserialize_json(data: dict) -> ThumbnailDetail:
    out: ThumbnailDetail = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    if "thumbnails" in data:
        import aws_sdk_medialive.types.__list_of_thumbnail

        out["thumbnails"] = (
            aws_sdk_medialive.types.__list_of_thumbnail.deserialize_json(
                data["thumbnails"]
            )
        )
    return out
