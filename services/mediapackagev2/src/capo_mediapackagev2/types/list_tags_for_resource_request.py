"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.tag_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediapackagev2.types.tag_arn.TagArn"
    """<p>The ARN of the CloudWatch resource that you want to view tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
