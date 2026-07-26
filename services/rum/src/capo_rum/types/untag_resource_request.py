"""Generated from Smithy shape ``com.amazonaws.rum#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rum.types.arn
    import capo_rum.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rum.types.arn.Arn"
    """<p>The ARN of the CloudWatch RUM resource that you're removing tags from.</p>"""
    tag_keys: "capo_rum.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
