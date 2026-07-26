"""Generated from Smithy shape ``com.amazonaws.schemas#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__list_of__string
    import capo_schemas.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_schemas.types.__string.__string"
    """<p>The ARN of the resource.</p>"""
    tag_keys: NotRequired["capo_schemas.types.__list_of__string.__listOf__string"]
    """<p>Keys of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
