"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.arn


class ListTagsRequest(TypedDict, closed=True):
    arn: "aws_sdk_elasticsearch_service.types.arn.ARN"
    """<p> Specify the <code>ARN</code> for the Elasticsearch domain to which the tags are attached that you want to view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
