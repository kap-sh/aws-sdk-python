"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to get a list of tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
