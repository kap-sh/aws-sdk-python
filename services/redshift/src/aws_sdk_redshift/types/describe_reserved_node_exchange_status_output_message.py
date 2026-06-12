"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeReservedNodeExchangeStatusOutputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.reserved_node_exchange_status_list
    import aws_sdk_redshift.types.string


class DescribeReservedNodeExchangeStatusOutputMessage(TypedDict):
    reserved_node_exchange_status_details: NotRequired[
        "aws_sdk_redshift.types.reserved_node_exchange_status_list.ReservedNodeExchangeStatusList"
    ]
    """<p>The details of the reserved-node exchange request, including the status, request time, source reserved-node identifier, and additional details.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A pagination token provided by a previous <code>DescribeReservedNodeExchangeStatus</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReservedNodeExchangeStatusOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_node_exchange_status_details" in value:
        import aws_sdk_redshift.types.reserved_node_exchange_status_list

        aws_sdk_redshift.types.reserved_node_exchange_status_list.serialize_query(
            value["reserved_node_exchange_status_details"],
            pairs,
            f"{prefix}.ReservedNodeExchangeStatusDetails",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeReservedNodeExchangeStatusOutputMessage:
    out: DescribeReservedNodeExchangeStatusOutputMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_exchange_status_details = el.find(
        "ReservedNodeExchangeStatusDetails"
    )
    if child_reserved_node_exchange_status_details is not None:
        import aws_sdk_redshift.types.reserved_node_exchange_status_list

        out["reserved_node_exchange_status_details"] = (
            aws_sdk_redshift.types.reserved_node_exchange_status_list.deserialize_query(
                child_reserved_node_exchange_status_details
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
