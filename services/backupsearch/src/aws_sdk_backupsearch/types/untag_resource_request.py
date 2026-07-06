"""Generated from Smithy shape ``com.amazonaws.backupsearch#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the resource where you want to remove tags.</p>"""
    tag_keys: "aws_sdk_backupsearch.types.tag_keys.TagKeys"
    """<p>This required parameter contains the tag keys you want to remove from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
