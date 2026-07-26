"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListSignalCatalogNodesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_node_type


class ListSignalCatalogNodesRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to list information about. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired["capo_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    signal_node_type: NotRequired[
        "capo_iotfleetwise.types.signal_node_type.SignalNodeType"
    ]
    """<p>The type of node in the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSignalCatalogNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSignalCatalogNodesRequest:
    out: ListSignalCatalogNodesRequest = {}  # type: ignore[typeddict-item]
    return out
