"""Generated from Smithy shape ``com.amazonaws.kafka#ListReplicatorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.max_results


class ListReplicatorsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators.</p>"""
    replicator_name_filter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Returns replicators starting with given name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicatorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReplicatorsRequest:
    out: ListReplicatorsRequest = {}  # type: ignore[typeddict-item]
    return out
