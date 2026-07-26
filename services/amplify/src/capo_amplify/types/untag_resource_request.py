"""Generated from Smithy shape ``com.amazonaws.amplify#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.resource_arn
    import capo_amplify.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_amplify.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) to use to untag a resource. </p>"""
    tag_keys: "capo_amplify.types.tag_key_list.TagKeyList"
    """<p>The tag keys to use to untag a resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
