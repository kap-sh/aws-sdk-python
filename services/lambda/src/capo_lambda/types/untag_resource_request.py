"""Generated from Smithy shape ``com.amazonaws.lambda#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.tag_key_list
    import capo_lambda.types.taggable_resource


class UntagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda.types.taggable_resource.TaggableResource"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_lambda.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
