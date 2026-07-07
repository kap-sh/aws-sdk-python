"""Generated from Smithy shape ``com.amazonaws.appconfig#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_appconfig.types.arn.Arn"
    """<p>The ARN of the resource for which to remove tags.</p>"""
    tag_keys: "aws_sdk_appconfig.types.tag_key_list.TagKeyList"
    """<p>The tag keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
