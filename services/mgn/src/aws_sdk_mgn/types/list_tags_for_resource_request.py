"""Generated from Smithy shape ``com.amazonaws.mgn#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_mgn.types.arn.ARN"
    """<p>List tags for resource request by ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
