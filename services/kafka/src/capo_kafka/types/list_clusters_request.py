"""Generated from Smithy shape ``com.amazonaws.kafka#ListClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListClustersRequest(TypedDict, closed=True):
    cluster_name_filter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>"""
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClustersRequest:
    out: ListClustersRequest = {}  # type: ignore[typeddict-item]
    return out
