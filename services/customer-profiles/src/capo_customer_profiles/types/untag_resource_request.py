"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.tag_arn
    import capo_customer_profiles.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_customer_profiles.types.tag_arn.TagArn"
    """<p>The ARN of the resource from which you are removing tags.</p>"""
    tag_keys: "capo_customer_profiles.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
