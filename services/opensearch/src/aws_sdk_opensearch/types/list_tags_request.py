"""Generated from Smithy shape ``com.amazonaws.opensearch#ListTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn


class ListTagsRequest(TypedDict):
    arn: "aws_sdk_opensearch.types.arn.ARN"
    """<p>Amazon Resource Name (ARN) for the domain, data source, or application to view tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
