"""Generated from Smithy shape ``com.amazonaws.fis#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.resource_arn
    import aws_sdk_fis.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_fis.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["aws_sdk_fis.types.tag_key_list.TagKeyList"]
    """<p>The tag keys to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
