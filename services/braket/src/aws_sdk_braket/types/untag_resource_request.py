"""Generated from Smithy shape ``com.amazonaws.braket#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_braket.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>Specify the <code>resourceArn</code> for the resource from which to remove the tags.</p>"""
    tag_keys: "aws_sdk_braket.types.tag_keys.TagKeys"
    """<p>Specify the keys for the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
