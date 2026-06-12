"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a specific resource in your Resilience Hub application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
