"""Generated from Smithy shape ``com.amazonaws.kafka#ListClustersV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.max_results


class ListClustersV2Request(TypedDict, closed=True):
    cluster_name_filter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Specify a prefix of the names of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>"""
    cluster_type_filter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Specify either PROVISIONED or SERVERLESS.</p>"""
    max_results: NotRequired["aws_sdk_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClustersV2Request:
    out: ListClustersV2Request = {}  # type: ignore[typeddict-item]
    return out
