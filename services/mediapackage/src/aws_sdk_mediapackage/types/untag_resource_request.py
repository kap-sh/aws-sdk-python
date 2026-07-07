"""Generated from Smithy shape ``com.amazonaws.mediapackage#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__list_of__string
    import aws_sdk_mediapackage.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_mediapackage.types.__string.__string"
    tag_keys: NotRequired[
        "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
    ]
    """The key(s) of tag to be deleted"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
