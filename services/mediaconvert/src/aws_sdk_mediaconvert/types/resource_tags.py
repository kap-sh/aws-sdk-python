"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ResourceTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string


class ResourceTags(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the resource."""
    tags: NotRequired["aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"]
    """The tags for the resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTags) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ResourceTags:
    out: ResourceTags = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
