"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.double
    import capo_redshift.types.integer
    import capo_redshift.types.recurring_charge_list
    import capo_redshift.types.reserved_node_offering_type
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class ReservedNode(TypedDict, closed=True):
    reserved_node_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the reservation.</p>"""
    reserved_node_offering_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier for the reserved node offering.</p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type of the reserved node.</p>"""
    start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.</p>"""
    duration: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The duration of the node reservation in seconds.</p>"""
    fixed_price: NotRequired["capo_redshift.types.double.Double"]
    """<p>The fixed cost Amazon Redshift charges you for this reserved node.</p>"""
    usage_price: NotRequired["capo_redshift.types.double.Double"]
    """<p>The hourly rate Amazon Redshift charges you for this reserved node.</p>"""
    currency_code: NotRequired["capo_redshift.types.string.String"]
    """<p>The currency code for the reserved cluster.</p>"""
    node_count: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of reserved compute nodes.</p>"""
    state: NotRequired["capo_redshift.types.string.String"]
    """<p>The state of the reserved compute node.</p> <p>Possible Values:</p> <ul> <li> <p>pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.</p> </li> <li> <p>active-This reserved node is owned by the caller and is available for use.</p> </li> <li> <p>payment-failed-Payment failed for the purchase attempt.</p> </li> <li> <p>retired-The reserved node is no longer available. </p> </li> <li> <p>exchanging-The owner is exchanging the reserved node for another reserved node.</p> </li> </ul>"""
    offering_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The anticipated utilization of the reserved node, as defined in the reserved node offering.</p>"""
    recurring_charges: NotRequired[
        "capo_redshift.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring charges for the reserved node.</p>"""
    reserved_node_offering_type: NotRequired[
        "capo_redshift.types.reserved_node_offering_type.ReservedNodeOfferingType"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_node_id" in value:
        pairs.append((f"{key_prefix}ReservedNodeId", str(value["reserved_node_id"])))
    if "reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedNodeOfferingId",
                str(value["reserved_node_offering_id"]),
            )
        )
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "fixed_price" in value:
        pairs.append((f"{key_prefix}FixedPrice", str(value["fixed_price"])))
    if "usage_price" in value:
        pairs.append((f"{key_prefix}UsagePrice", str(value["usage_price"])))
    if "currency_code" in value:
        pairs.append((f"{key_prefix}CurrencyCode", str(value["currency_code"])))
    if "node_count" in value:
        pairs.append((f"{key_prefix}NodeCount", str(value["node_count"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "offering_type" in value:
        pairs.append((f"{key_prefix}OfferingType", str(value["offering_type"])))
    if "recurring_charges" in value:
        import capo_redshift.types.recurring_charge_list

        capo_redshift.types.recurring_charge_list.serialize_query(
            value["recurring_charges"], pairs, f"{key_prefix}RecurringCharges"
        )
    if "reserved_node_offering_type" in value:
        import capo_redshift.types.reserved_node_offering_type

        capo_redshift.types.reserved_node_offering_type.serialize_query(
            value["reserved_node_offering_type"],
            pairs,
            f"{key_prefix}ReservedNodeOfferingType",
        )


def deserialize_query(el: Element) -> ReservedNode:
    out: ReservedNode = {}  # type: ignore[typeddict-item]
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_reserved_node_offering_id = el.find("ReservedNodeOfferingId")
    if child_reserved_node_offering_id is not None:
        out["reserved_node_offering_id"] = str(
            child_reserved_node_offering_id.text or ""
        )
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_redshift.types.t_stamp

        out["start_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_fixed_price = el.find("FixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_usage_price = el.find("UsagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_node_count = el.find("NodeCount")
    if child_node_count is not None:
        out["node_count"] = int(child_node_count.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_recurring_charges = el.find("RecurringCharges")
    if child_recurring_charges is not None:
        import capo_redshift.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_redshift.types.recurring_charge_list.deserialize_query(
                child_recurring_charges
            )
        )
    child_reserved_node_offering_type = el.find("ReservedNodeOfferingType")
    if child_reserved_node_offering_type is not None:
        import capo_redshift.types.reserved_node_offering_type

        out["reserved_node_offering_type"] = (
            capo_redshift.types.reserved_node_offering_type.deserialize_query(
                child_reserved_node_offering_type
            )
        )
    return out
