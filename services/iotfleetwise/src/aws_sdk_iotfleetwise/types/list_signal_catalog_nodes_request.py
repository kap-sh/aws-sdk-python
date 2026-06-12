"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListSignalCatalogNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.max_results
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.signal_node_type


class ListSignalCatalogNodesRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to list information about. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired["aws_sdk_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    signal_node_type: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_node_type.SignalNodeType"
    ]
    """<p>The type of node in the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSignalCatalogNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSignalCatalogNodesRequest:
    out: ListSignalCatalogNodesRequest = {}  # type: ignore[typeddict-item]
    return out
