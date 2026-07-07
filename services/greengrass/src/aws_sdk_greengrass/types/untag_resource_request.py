"""Generated from Smithy shape ``com.amazonaws.greengrass#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of__string
    import aws_sdk_greengrass.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_greengrass.types.__string.__string"
    """The Amazon Resource Name (ARN) of the resource."""
    tag_keys: NotRequired["aws_sdk_greengrass.types.__list_of__string.__listOf__string"]
    """An array of tag keys to delete"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
