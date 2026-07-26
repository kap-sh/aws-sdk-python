"""Generated from Smithy shape ``com.amazonaws.greengrass#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of__string
    import capo_greengrass.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_greengrass.types.__string.__string"
    """The Amazon Resource Name (ARN) of the resource."""
    tag_keys: NotRequired["capo_greengrass.types.__list_of__string.__listOf__string"]
    """An array of tag keys to delete"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
