"""Generated from Smithy shape ``com.amazonaws.ivs#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.resource_arn
    import aws_sdk_ivs.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ivs.types.resource_arn.ResourceArn"
    """<p>ARN of the resource for which tags are to be removed. The ARN must be URL-encoded.</p>"""
    tag_keys: "aws_sdk_ivs.types.tag_key_list.TagKeyList"
    r"""<p>Array of tag keys (strings) for the tags to be removed. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
