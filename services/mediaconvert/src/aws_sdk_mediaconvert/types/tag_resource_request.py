"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string


class TagResourceRequest(TypedDict):
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the resource that you want to tag. To get the ARN, send a GET request with the resource name."""
    tags: NotRequired["aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"]
    """The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key."""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
