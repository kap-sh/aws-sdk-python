"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.rtb_taggable_resource_arn
    import capo_rtbfabric.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>"""
    tag_keys: "capo_rtbfabric.types.tag_key_list.TagKeyList"
    """<p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
