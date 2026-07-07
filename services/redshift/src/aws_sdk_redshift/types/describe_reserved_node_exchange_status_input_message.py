"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeReservedNodeExchangeStatusInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeReservedNodeExchangeStatusInputMessage(TypedDict, closed=True):
    reserved_node_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the source reserved node in a reserved-node exchange request.</p>"""
    reserved_node_exchange_request_id: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The identifier of the reserved-node exchange request.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>Marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeReservedNodeExchangeStatus</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReservedNodeExchangeStatusInputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_node_id" in value:
        pairs.append((f"{prefix}.ReservedNodeId", str(value["reserved_node_id"])))
    if "reserved_node_exchange_request_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedNodeExchangeRequestId",
                str(value["reserved_node_exchange_request_id"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeReservedNodeExchangeStatusInputMessage:
    out: DescribeReservedNodeExchangeStatusInputMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_reserved_node_exchange_request_id = el.find("ReservedNodeExchangeRequestId")
    if child_reserved_node_exchange_request_id is not None:
        out["reserved_node_exchange_request_id"] = str(
            child_reserved_node_exchange_request_id.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
