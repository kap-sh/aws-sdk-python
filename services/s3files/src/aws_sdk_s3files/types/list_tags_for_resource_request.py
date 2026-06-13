"""Generated from Smithy shape ``com.amazonaws.s3files#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3files.types.resource_id


class ListTagsForResourceRequest(TypedDict):
    resource_id: "aws_sdk_s3files.types.resource_id.ResourceId"
    """<p>The ID or Amazon Resource Name (ARN) of the resource to list tags for.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of tags to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token returned from a previous call to continue listing tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
