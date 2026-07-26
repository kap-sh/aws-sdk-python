"""Generated from Smithy shape ``com.amazonaws.opensearch#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn


class ListTagsRequest(TypedDict, closed=True):
    arn: "capo_opensearch.types.arn.ARN"
    """<p>Amazon Resource Name (ARN) for the domain, data source, or application to view tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
