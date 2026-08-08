"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesListingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.filter_list
    import capo_ec2.types.reservation_id
    import capo_ec2.types.reserved_instances_listing_id


class DescribeReservedInstancesListingsRequest(TypedDict, closed=True):
    reserved_instances_id: NotRequired["capo_ec2.types.reservation_id.ReservationId"]
    """<p>One or more Reserved Instance IDs.</p>"""
    reserved_instances_listing_id: NotRequired[
        "capo_ec2.types.reserved_instances_listing_id.ReservedInstancesListingId"
    ]
    """<p>One or more Reserved Instance listing IDs.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>reserved-instances-id</code> - The ID of the Reserved Instances.</p> </li> <li> <p> <code>reserved-instances-listing-id</code> - The ID of the Reserved Instances listing.</p> </li> <li> <p> <code>status</code> - The status of the Reserved Instance listing (<code>pending</code> | <code>active</code> | <code>cancelled</code> | <code>closed</code>).</p> </li> <li> <p> <code>status-message</code> - The reason for the status.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesListingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "reserved_instances_listing_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedInstancesListingId",
                str(value["reserved_instances_listing_id"]),
            )
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesListingsRequest:
    out: DescribeReservedInstancesListingsRequest = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("reservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_reserved_instances_listing_id = el.find("reservedInstancesListingId")
    if child_reserved_instances_listing_id is not None:
        out["reserved_instances_listing_id"] = str(
            child_reserved_instances_listing_id.text or ""
        )
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    return out
