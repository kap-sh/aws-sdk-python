"""Generated from Smithy shape ``com.amazonaws.outposts#OrderSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.iso8601_timestamp
    import capo_outposts.types.line_item_status_counts
    import capo_outposts.types.order_id
    import capo_outposts.types.order_status
    import capo_outposts.types.order_type
    import capo_outposts.types.outpost_id_only


class OrderSummary(TypedDict, closed=True):
    outpost_id: NotRequired["capo_outposts.types.outpost_id_only.OutpostIdOnly"]
    """<p> The ID of the Outpost. </p>"""
    order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p> The ID of the order. </p>"""
    order_type: NotRequired["capo_outposts.types.order_type.OrderType"]
    """<p>The type of order.</p>"""
    status: NotRequired["capo_outposts.types.order_status.OrderStatus"]
    """<p>The status of the order.</p> <ul> <li> <p> <code>PREPARING</code> - Order is received and is being prepared.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Order is either being built, shipped, or installed. For more information, see the <code>LineItem</code> status.</p> </li> <li> <p> <code>COMPLETED</code> - Order is complete.</p> </li> <li> <p> <code>CANCELLED</code> - Order is cancelled.</p> </li> <li> <p> <code>ERROR</code> - Customer should contact support.</p> </li> </ul> <note> <p>The following statuses are deprecated: <code>RECEIVED</code>, <code>PENDING</code>, <code>PROCESSING</code>, <code>INSTALLING</code>, and <code>FULFILLED</code>. </p> </note>"""
    line_item_counts_by_status: NotRequired[
        "capo_outposts.types.line_item_status_counts.LineItemStatusCounts"
    ]
    """<p> The status of all line items in the order. </p>"""
    order_submission_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p> The submission date for the order. </p>"""
    order_fulfilled_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p> The fulfilment date for the order. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrderSummary) -> dict:
    out: dict = {}
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "order_type" in value:
        import capo_outposts.types.order_type

        out["OrderType"] = capo_outposts.types.order_type.serialize_json(
            value["order_type"]
        )
    if "status" in value:
        import capo_outposts.types.order_status

        out["Status"] = capo_outposts.types.order_status.serialize_json(value["status"])
    if "line_item_counts_by_status" in value:
        import capo_outposts.types.line_item_status_counts

        out["LineItemCountsByStatus"] = (
            capo_outposts.types.line_item_status_counts.serialize_json(
                value["line_item_counts_by_status"]
            )
        )
    if "order_submission_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["OrderSubmissionDate"] = (
            capo_outposts.types.iso8601_timestamp.serialize_json(
                value["order_submission_date"]
            )
        )
    if "order_fulfilled_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["OrderFulfilledDate"] = (
            capo_outposts.types.iso8601_timestamp.serialize_json(
                value["order_fulfilled_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrderSummary:
    out: OrderSummary = {}  # type: ignore[typeddict-item]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "OrderType" in data:
        import capo_outposts.types.order_type

        out["order_type"] = capo_outposts.types.order_type.deserialize_json(
            data["OrderType"]
        )
    if "Status" in data:
        import capo_outposts.types.order_status

        out["status"] = capo_outposts.types.order_status.deserialize_json(
            data["Status"]
        )
    if "LineItemCountsByStatus" in data:
        import capo_outposts.types.line_item_status_counts

        out["line_item_counts_by_status"] = (
            capo_outposts.types.line_item_status_counts.deserialize_json(
                data["LineItemCountsByStatus"]
            )
        )
    if "OrderSubmissionDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["order_submission_date"] = (
            capo_outposts.types.iso8601_timestamp.deserialize_json(
                data["OrderSubmissionDate"]
            )
        )
    if "OrderFulfilledDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["order_fulfilled_date"] = (
            capo_outposts.types.iso8601_timestamp.deserialize_json(
                data["OrderFulfilledDate"]
            )
        )
    return out
