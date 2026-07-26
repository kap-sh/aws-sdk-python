"""Generated from Smithy shape ``com.amazonaws.outposts#Order``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.iso8601_timestamp
    import capo_outposts.types.line_item_list_definition
    import capo_outposts.types.order_id
    import capo_outposts.types.order_status
    import capo_outposts.types.order_type
    import capo_outposts.types.outpost_id_only
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term


class Order(TypedDict, closed=True):
    outpost_id: NotRequired["capo_outposts.types.outpost_id_only.OutpostIdOnly"]
    """<p> The ID of the Outpost in the order. </p>"""
    order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p>The ID of the order.</p>"""
    status: NotRequired["capo_outposts.types.order_status.OrderStatus"]
    """<p>The status of the order.</p> <ul> <li> <p> <code>PREPARING</code> - Order is received and being prepared.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Order is either being built or shipped. To get more details, see the line item status.</p> </li> <li> <p> <code>DELIVERED</code> - Order was delivered to the Outpost site.</p> </li> <li> <p> <code>COMPLETED</code> - Order is complete.</p> </li> <li> <p> <code>CANCELLED</code> - Order is cancelled.</p> </li> <li> <p> <code>ERROR</code> - Customer should contact support.</p> </li> </ul> <note> <p>The following status are deprecated: <code>RECEIVED</code>, <code>PENDING</code>, <code>PROCESSING</code>, <code>INSTALLING</code>, and <code>FULFILLED</code>. </p> </note>"""
    line_items: NotRequired[
        "capo_outposts.types.line_item_list_definition.LineItemListDefinition"
    ]
    """<p>The line items for the order</p>"""
    payment_option: NotRequired["capo_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option for the order.</p>"""
    order_submission_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The submission date for the order.</p>"""
    order_fulfilled_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The fulfillment date of the order.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    order_type: NotRequired["capo_outposts.types.order_type.OrderType"]
    """<p>The type of order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Order) -> dict:
    out: dict = {}
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "status" in value:
        import capo_outposts.types.order_status

        out["Status"] = capo_outposts.types.order_status.serialize_json(value["status"])
    if "line_items" in value:
        import capo_outposts.types.line_item_list_definition

        out["LineItems"] = capo_outposts.types.line_item_list_definition.serialize_json(
            value["line_items"]
        )
    if "payment_option" in value:
        import capo_outposts.types.payment_option

        out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
            value["payment_option"]
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
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "order_type" in value:
        import capo_outposts.types.order_type

        out["OrderType"] = capo_outposts.types.order_type.serialize_json(
            value["order_type"]
        )
    return out


def deserialize_json(data: dict) -> Order:
    out: Order = {}  # type: ignore[typeddict-item]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "Status" in data:
        import capo_outposts.types.order_status

        out["status"] = capo_outposts.types.order_status.deserialize_json(
            data["Status"]
        )
    if "LineItems" in data:
        import capo_outposts.types.line_item_list_definition

        out["line_items"] = (
            capo_outposts.types.line_item_list_definition.deserialize_json(
                data["LineItems"]
            )
        )
    if "PaymentOption" in data:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
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
    if "PaymentTerm" in data:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "OrderType" in data:
        import capo_outposts.types.order_type

        out["order_type"] = capo_outposts.types.order_type.deserialize_json(
            data["OrderType"]
        )
    return out
