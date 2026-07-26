"""Generated from Smithy shape ``com.amazonaws.mediatailor#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of__string
    import capo_mediatailor.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource to untag.</p>"""
    tag_keys: "capo_mediatailor.types.__list_of__string.__listOf__string"
    """<p>The tag keys associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
