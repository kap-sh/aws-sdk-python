"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.rtb_taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
