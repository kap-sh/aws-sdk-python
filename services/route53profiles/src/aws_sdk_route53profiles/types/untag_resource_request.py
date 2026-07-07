"""Generated from Smithy shape ``com.amazonaws.route53profiles#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.arn
    import aws_sdk_route53profiles.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_route53profiles.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) for the resource that you want to remove tags from. </p>"""
    tag_keys: "aws_sdk_route53profiles.types.tag_key_list.TagKeyList"
    """<p> The tags that you want to remove to the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
