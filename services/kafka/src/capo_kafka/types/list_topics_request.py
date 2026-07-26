"""Generated from Smithy shape ``com.amazonaws.kafka#ListTopicsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListTopicsRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>"""
    topic_name_filter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Returns topics starting with given name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicsRequest:
    out: ListTopicsRequest = {}  # type: ignore[typeddict-item]
    return out
