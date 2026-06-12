"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.tag_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_customer_profiles.types.tag_arn.TagArn"
    """<p>The ARN of the resource for which you want to view tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
