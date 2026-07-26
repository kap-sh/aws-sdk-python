"""Generated from Smithy shape ``com.amazonaws.finspace#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.fin_space_taggable_arn
    import capo_finspace.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn"
    """<p>A FinSpace resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_finspace.types.tag_key_list.TagKeyList"
    """<p>The tag keys (names) of one or more tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
