"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.max_results


class ListConnectorsRequest(TypedDict, closed=True):
    connector_name_prefix: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The name prefix that you want to use to search for and list connectors.</p>"""
    max_results: NotRequired["capo_kafkaconnect.types.max_results.MaxResults"]
    """<p>The maximum number of connectors to list in one response.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
