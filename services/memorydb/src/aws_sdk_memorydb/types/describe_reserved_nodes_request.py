"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeReservedNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string


class DescribeReservedNodesRequest(TypedDict):
    reservation_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The reserved node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.</p>"""
    reserved_nodes_offering_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.</p>"""
    node_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The node type filter value. Use this parameter to show only those reservations matching the specified node type. For more information, see <a href=\"https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported\">Supported node types</a>.</p>"""
    duration: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.</p>"""
    offering_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: \"All Upfront\"|\"Partial Upfront\"| \"No Upfront\"</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedNodesRequest) -> dict:
    out: dict = {}
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedNodesRequest:
    out: DescribeReservedNodesRequest = {}  # type: ignore[typeddict-item]
    if "ReservationId" in data:
        out["reservation_id"] = data["ReservationId"]
    if "ReservedNodesOfferingId" in data:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "OfferingType" in data:
        out["offering_type"] = data["OfferingType"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
