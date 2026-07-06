"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_deployment.types.string_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>"""
    tag_keys: "aws_sdk_marketplace_deployment.types.string_list.StringList"
    """<p>A list of key names of tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
