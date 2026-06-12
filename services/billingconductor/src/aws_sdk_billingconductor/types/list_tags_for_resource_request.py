"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_billingconductor.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) that identifies the resource to list the tags. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
