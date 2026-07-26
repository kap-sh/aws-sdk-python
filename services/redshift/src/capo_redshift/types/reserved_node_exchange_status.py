"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer
    import capo_redshift.types.reserved_node_exchange_status_type
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class ReservedNodeExchangeStatus(TypedDict, closed=True):
    reserved_node_exchange_request_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the reserved-node exchange request.</p>"""
    status: NotRequired[
        "capo_redshift.types.reserved_node_exchange_status_type.ReservedNodeExchangeStatusType"
    ]
    """<p>The status of the reserved-node exchange request. Statuses include in-progress and requested.</p>"""
    request_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>A date and time that indicate when the reserved-node exchange was requested.</p>"""
    source_reserved_node_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the source reserved node.</p>"""
    source_reserved_node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The source reserved-node type, for example ra3.4xlarge.</p>"""
    source_reserved_node_count: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The source reserved-node count in the cluster.</p>"""
    target_reserved_node_offering_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the target reserved node offering.</p>"""
    target_reserved_node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type of the target reserved node, for example ra3.4xlarge.</p>"""
    target_reserved_node_count: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The count of target reserved nodes in the cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeExchangeStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_node_exchange_request_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedNodeExchangeRequestId",
                str(value["reserved_node_exchange_request_id"]),
            )
        )
    if "status" in value:
        import capo_redshift.types.reserved_node_exchange_status_type

        capo_redshift.types.reserved_node_exchange_status_type.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "request_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["request_time"], pairs, f"{prefix}.RequestTime"
        )
    if "source_reserved_node_id" in value:
        pairs.append(
            (f"{prefix}.SourceReservedNodeId", str(value["source_reserved_node_id"]))
        )
    if "source_reserved_node_type" in value:
        pairs.append(
            (
                f"{prefix}.SourceReservedNodeType",
                str(value["source_reserved_node_type"]),
            )
        )
    if "source_reserved_node_count" in value:
        pairs.append(
            (
                f"{prefix}.SourceReservedNodeCount",
                str(value["source_reserved_node_count"]),
            )
        )
    if "target_reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeOfferingId",
                str(value["target_reserved_node_offering_id"]),
            )
        )
    if "target_reserved_node_type" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeType",
                str(value["target_reserved_node_type"]),
            )
        )
    if "target_reserved_node_count" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeCount",
                str(value["target_reserved_node_count"]),
            )
        )


def deserialize_query(el: Element) -> ReservedNodeExchangeStatus:
    out: ReservedNodeExchangeStatus = {}  # type: ignore[typeddict-item]
    child_reserved_node_exchange_request_id = el.find("ReservedNodeExchangeRequestId")
    if child_reserved_node_exchange_request_id is not None:
        out["reserved_node_exchange_request_id"] = str(
            child_reserved_node_exchange_request_id.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.reserved_node_exchange_status_type

        out["status"] = (
            capo_redshift.types.reserved_node_exchange_status_type.deserialize_query(
                child_status
            )
        )
    child_request_time = el.find("RequestTime")
    if child_request_time is not None:
        import capo_redshift.types.t_stamp

        out["request_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_request_time
        )
    child_source_reserved_node_id = el.find("SourceReservedNodeId")
    if child_source_reserved_node_id is not None:
        out["source_reserved_node_id"] = str(child_source_reserved_node_id.text or "")
    child_source_reserved_node_type = el.find("SourceReservedNodeType")
    if child_source_reserved_node_type is not None:
        out["source_reserved_node_type"] = str(
            child_source_reserved_node_type.text or ""
        )
    child_source_reserved_node_count = el.find("SourceReservedNodeCount")
    if child_source_reserved_node_count is not None:
        out["source_reserved_node_count"] = int(
            child_source_reserved_node_count.text or ""
        )
    child_target_reserved_node_offering_id = el.find("TargetReservedNodeOfferingId")
    if child_target_reserved_node_offering_id is not None:
        out["target_reserved_node_offering_id"] = str(
            child_target_reserved_node_offering_id.text or ""
        )
    child_target_reserved_node_type = el.find("TargetReservedNodeType")
    if child_target_reserved_node_type is not None:
        out["target_reserved_node_type"] = str(
            child_target_reserved_node_type.text or ""
        )
    child_target_reserved_node_count = el.find("TargetReservedNodeCount")
    if child_target_reserved_node_count is not None:
        out["target_reserved_node_count"] = int(
            child_target_reserved_node_count.text or ""
        )
    return out
