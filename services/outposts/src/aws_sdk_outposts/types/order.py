"""Generated from Smithy shape ``com.amazonaws.outposts#Order``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.iso8601_timestamp
    import aws_sdk_outposts.types.line_item_list_definition
    import aws_sdk_outposts.types.order_id
    import aws_sdk_outposts.types.order_status
    import aws_sdk_outposts.types.order_type
    import aws_sdk_outposts.types.outpost_id_only
    import aws_sdk_outposts.types.payment_option
    import aws_sdk_outposts.types.payment_term


class Order(TypedDict):
    outpost_id: NotRequired["aws_sdk_outposts.types.outpost_id_only.OutpostIdOnly"]
    """<p> The ID of the Outpost in the order. </p>"""
    order_id: NotRequired["aws_sdk_outposts.types.order_id.OrderId"]
    """<p>The ID of the order.</p>"""
    status: NotRequired["aws_sdk_outposts.types.order_status.OrderStatus"]
    """<p>The status of the order.</p> <ul> <li> <p> <code>PREPARING</code> - Order is received and being prepared.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Order is either being built or shipped. To get more details, see the line item status.</p> </li> <li> <p> <code>DELIVERED</code> - Order was delivered to the Outpost site.</p> </li> <li> <p> <code>COMPLETED</code> - Order is complete.</p> </li> <li> <p> <code>CANCELLED</code> - Order is cancelled.</p> </li> <li> <p> <code>ERROR</code> - Customer should contact support.</p> </li> </ul> <note> <p>The following status are deprecated: <code>RECEIVED</code>, <code>PENDING</code>, <code>PROCESSING</code>, <code>INSTALLING</code>, and <code>FULFILLED</code>. </p> </note>"""
    line_items: NotRequired[
        "aws_sdk_outposts.types.line_item_list_definition.LineItemListDefinition"
    ]
    """<p>The line items for the order</p>"""
    payment_option: NotRequired["aws_sdk_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option for the order.</p>"""
    order_submission_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The submission date for the order.</p>"""
    order_fulfilled_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The fulfillment date of the order.</p>"""
    payment_term: NotRequired["aws_sdk_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    order_type: NotRequired["aws_sdk_outposts.types.order_type.OrderType"]
    """<p>The type of order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Order) -> dict:
    out: dict = {}
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "status" in value:
        import aws_sdk_outposts.types.order_status

        out["Status"] = aws_sdk_outposts.types.order_status.serialize_json(
            value["status"]
        )
    if "line_items" in value:
        import aws_sdk_outposts.types.line_item_list_definition

        out["LineItems"] = (
            aws_sdk_outposts.types.line_item_list_definition.serialize_json(
                value["line_items"]
            )
        )
    if "payment_option" in value:
        import aws_sdk_outposts.types.payment_option

        out["PaymentOption"] = aws_sdk_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    if "order_submission_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["OrderSubmissionDate"] = (
            aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
                value["order_submission_date"]
            )
        )
    if "order_fulfilled_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["OrderFulfilledDate"] = (
            aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
                value["order_fulfilled_date"]
            )
        )
    if "payment_term" in value:
        import aws_sdk_outposts.types.payment_term

        out["PaymentTerm"] = aws_sdk_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "order_type" in value:
        import aws_sdk_outposts.types.order_type

        out["OrderType"] = aws_sdk_outposts.types.order_type.serialize_json(
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
        import aws_sdk_outposts.types.order_status

        out["status"] = aws_sdk_outposts.types.order_status.deserialize_json(
            data["Status"]
        )
    if "LineItems" in data:
        import aws_sdk_outposts.types.line_item_list_definition

        out["line_items"] = (
            aws_sdk_outposts.types.line_item_list_definition.deserialize_json(
                data["LineItems"]
            )
        )
    if "PaymentOption" in data:
        import aws_sdk_outposts.types.payment_option

        out["payment_option"] = aws_sdk_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    if "OrderSubmissionDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["order_submission_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["OrderSubmissionDate"]
            )
        )
    if "OrderFulfilledDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["order_fulfilled_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["OrderFulfilledDate"]
            )
        )
    if "PaymentTerm" in data:
        import aws_sdk_outposts.types.payment_term

        out["payment_term"] = aws_sdk_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "OrderType" in data:
        import aws_sdk_outposts.types.order_type

        out["order_type"] = aws_sdk_outposts.types.order_type.deserialize_json(
            data["OrderType"]
        )
    return out
