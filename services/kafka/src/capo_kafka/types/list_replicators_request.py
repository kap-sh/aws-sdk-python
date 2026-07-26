"""Generated from Smithy shape ``com.amazonaws.kafka#ListReplicatorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListReplicatorsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators.</p>"""
    replicator_name_filter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Returns replicators starting with given name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicatorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReplicatorsRequest:
    out: ListReplicatorsRequest = {}  # type: ignore[typeddict-item]
    return out
