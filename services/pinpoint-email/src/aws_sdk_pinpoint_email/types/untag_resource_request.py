"""Generated from Smithy shape ``com.amazonaws.pinpointemail#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.amazon_resource_name
    import aws_sdk_pinpoint_email.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_pinpoint_email.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.</p>"""
    tag_keys: "aws_sdk_pinpoint_email.types.tag_key_list.TagKeyList"
    """<p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the resource, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. For example: <code>/v1/email/tags?ResourceArn=ResourceArn&TagKeys=Key1&TagKeys=Key2</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
