"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline's region, resource ID, and pipeline ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
