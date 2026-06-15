"""Generated from Smithy shape ``com.amazonaws.greengrassv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.generic_v2_arn
    import aws_sdk_greengrassv2.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_greengrassv2.types.generic_v2_arn.GenericV2ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to untag.</p>"""
    tag_keys: "aws_sdk_greengrassv2.types.tag_key_list.TagKeyList"
    """<p>A list of keys for tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
