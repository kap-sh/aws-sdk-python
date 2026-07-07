"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.double
    import aws_sdk_memorydb.types.integer
    import aws_sdk_memorydb.types.recurring_charge_list
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.t_stamp


class ReservedNode(TypedDict, closed=True):
    reservation_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A customer-specified identifier to track this reservation.</p>"""
    reserved_nodes_offering_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The ID of the reserved node offering to purchase.</p>"""
    node_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The node type for the reserved nodes.</p>"""
    start_time: NotRequired["aws_sdk_memorydb.types.t_stamp.TStamp"]
    """<p>The time the reservation started.</p>"""
    duration: "aws_sdk_memorydb.types.integer.Integer"
    """<p>The duration of the reservation in seconds.</p>"""
    fixed_price: "aws_sdk_memorydb.types.double.Double"
    """<p>The fixed price charged for this reserved node.</p>"""
    node_count: "aws_sdk_memorydb.types.integer.Integer"
    """<p>The number of nodes that have been reserved.</p>"""
    offering_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The offering type of this reserved node.</p>"""
    state: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The state of the reserved node.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_memorydb.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved node.</p>"""
    arn: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the reserved node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNode) -> dict:
    out: dict = {}
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "start_time" in value:
        import aws_sdk_memorydb.types.t_stamp

        out["StartTime"] = aws_sdk_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["Duration"] = value.get("duration", 0)
    out["FixedPrice"] = value.get("fixed_price", 0)
    out["NodeCount"] = value.get("node_count", 0)
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "state" in value:
        out["State"] = value["state"]
    if "recurring_charges" in value:
        import aws_sdk_memorydb.types.recurring_charge_list

        out["RecurringCharges"] = (
            aws_sdk_memorydb.types.recurring_charge_list.serialize_aws_json_1_1(
                value["recurring_charges"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedNode:
    out: ReservedNode = {}  # type: ignore[typeddict-item]
    if "ReservationId" in data:
        out["reservation_id"] = data["ReservationId"]
    if "ReservedNodesOfferingId" in data:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "StartTime" in data:
        import aws_sdk_memorydb.types.t_stamp

        out["start_time"] = aws_sdk_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "FixedPrice" in data:
        out["fixed_price"] = data["FixedPrice"]
    else:
        out["fixed_price"] = 0
    if "NodeCount" in data:
        out["node_count"] = data["NodeCount"]
    else:
        out["node_count"] = 0
    if "OfferingType" in data:
        out["offering_type"] = data["OfferingType"]
    if "State" in data:
        out["state"] = data["State"]
    if "RecurringCharges" in data:
        import aws_sdk_memorydb.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_memorydb.types.recurring_charge_list.deserialize_aws_json_1_1(
                data["RecurringCharges"]
            )
        )
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
