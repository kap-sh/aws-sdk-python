"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__list_of__string
    import aws_sdk_mediapackage_vod.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource."""
    tag_keys: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of__string.__listOf__string"
    ]
    """A comma-separated list of the tag keys to remove from the resource."""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
