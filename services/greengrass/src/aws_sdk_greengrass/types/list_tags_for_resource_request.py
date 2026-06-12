"""Generated from Smithy shape ``com.amazonaws.greengrass#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_greengrass.types.__string.__string"
    """The Amazon Resource Name (ARN) of the resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
