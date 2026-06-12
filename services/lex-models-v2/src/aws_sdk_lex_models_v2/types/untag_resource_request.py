"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to remove the tags from.</p>"""
    tag_keys: "aws_sdk_lex_models_v2.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
