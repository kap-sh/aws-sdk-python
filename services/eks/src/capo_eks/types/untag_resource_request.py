"""Generated from Smithy shape ``com.amazonaws.eks#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>"""
    tag_keys: "capo_eks.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
