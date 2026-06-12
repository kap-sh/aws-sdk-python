"""Generated from Smithy shape ``com.amazonaws.securityhub#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to retrieve tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
