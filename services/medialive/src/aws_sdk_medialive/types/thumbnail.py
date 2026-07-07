"""Generated from Smithy shape ``com.amazonaws.medialive#Thumbnail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__timestamp_iso8601
    import aws_sdk_medialive.types.thumbnail_type


class Thumbnail(TypedDict, closed=True):
    body: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The binary data for the latest thumbnail."""
    content_type: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The content type for the latest thumbnail."""
    thumbnail_type: NotRequired["aws_sdk_medialive.types.thumbnail_type.ThumbnailType"]
    """Thumbnail Type"""
    time_stamp: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """Time stamp for the latest thumbnail."""


# --- restJson1 ser/de ---
def serialize_json(value: Thumbnail) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "thumbnail_type" in value:
        import aws_sdk_medialive.types.thumbnail_type

        out["thumbnailType"] = aws_sdk_medialive.types.thumbnail_type.serialize_json(
            value["thumbnail_type"]
        )
    if "time_stamp" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["timeStamp"] = aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
            value["time_stamp"]
        )
    return out


def deserialize_json(data: dict) -> Thumbnail:
    out: Thumbnail = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "thumbnailType" in data:
        import aws_sdk_medialive.types.thumbnail_type

        out["thumbnail_type"] = aws_sdk_medialive.types.thumbnail_type.deserialize_json(
            data["thumbnailType"]
        )
    if "timeStamp" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["time_stamp"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["timeStamp"]
            )
        )
    return out
