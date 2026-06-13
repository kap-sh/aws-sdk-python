"""Generated from Smithy shape ``com.amazonaws.groundstation#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.any_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn"
    """<p>ARN of a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
