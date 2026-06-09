"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_id
    import aws_sdk_ec2.types.capacity_block_interconnect_status
    import aws_sdk_ec2.types.capacity_reservation_status_set
    import aws_sdk_ec2.types.integer


class CapacityBlockStatus(TypedDict):
    capacity_block_id: NotRequired[
        "aws_sdk_ec2.types.capacity_block_id.CapacityBlockId"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    interconnect_status: NotRequired[
        "aws_sdk_ec2.types.capacity_block_interconnect_status.CapacityBlockInterconnectStatus"
    ]
    """<p>The status of the high-bandwidth accelerator interconnect. Possible states include:</p> <ul> <li> <p> <code>ok</code> the accelerator interconnect is healthy.</p> </li> <li> <p> <code>impaired</code> - accelerator interconnect communication is impaired.</p> </li> <li> <p> <code>insufficient-data</code> - insufficient data to determine accelerator interconnect status.</p> </li> </ul>"""
    total_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The combined amount of <code>Available</code> and <code>Unavailable</code> capacity in the Capacity Block.</p>"""
    total_available_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of resources that can be launched into the Capacity Block.</p>"""
    total_unavailable_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The unavailable capacity. Indicates the instance capacity that is unavailable for use due to a system status check failure.</p>"""
    capacity_reservation_statuses: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_status_set.CapacityReservationStatusSet"
    ]
    """<p>The availability of capacity for the Capacity Block reservations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_block_id" in value:
        pairs.append((f"{prefix}.CapacityBlockId", str(value["capacity_block_id"])))
    if "interconnect_status" in value:
        import aws_sdk_ec2.types.capacity_block_interconnect_status

        aws_sdk_ec2.types.capacity_block_interconnect_status.serialize_ec2_query(
            value["interconnect_status"], pairs, f"{prefix}.InterconnectStatus"
        )
    if "total_capacity" in value:
        pairs.append((f"{prefix}.TotalCapacity", str(value["total_capacity"])))
    if "total_available_capacity" in value:
        pairs.append(
            (f"{prefix}.TotalAvailableCapacity", str(value["total_available_capacity"]))
        )
    if "total_unavailable_capacity" in value:
        pairs.append(
            (
                f"{prefix}.TotalUnavailableCapacity",
                str(value["total_unavailable_capacity"]),
            )
        )
    if "capacity_reservation_statuses" in value:
        import aws_sdk_ec2.types.capacity_reservation_status_set

        aws_sdk_ec2.types.capacity_reservation_status_set.serialize_ec2_query(
            value["capacity_reservation_statuses"],
            pairs,
            f"{prefix}.CapacityReservationStatusSet",
        )


def deserialize_ec2_query(el: Element) -> CapacityBlockStatus:
    out: CapacityBlockStatus = {}  # type: ignore[typeddict-item]
    child_capacity_block_id = el.find("CapacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_interconnect_status = el.find("InterconnectStatus")
    if child_interconnect_status is not None:
        import aws_sdk_ec2.types.capacity_block_interconnect_status

        out["interconnect_status"] = (
            aws_sdk_ec2.types.capacity_block_interconnect_status.deserialize_ec2_query(
                child_interconnect_status
            )
        )
    child_total_capacity = el.find("TotalCapacity")
    if child_total_capacity is not None:
        out["total_capacity"] = int(child_total_capacity.text or "")
    child_total_available_capacity = el.find("TotalAvailableCapacity")
    if child_total_available_capacity is not None:
        out["total_available_capacity"] = int(child_total_available_capacity.text or "")
    child_total_unavailable_capacity = el.find("TotalUnavailableCapacity")
    if child_total_unavailable_capacity is not None:
        out["total_unavailable_capacity"] = int(
            child_total_unavailable_capacity.text or ""
        )
    if el.find("CapacityReservationStatusSet") is not None:
        import aws_sdk_ec2.types.capacity_reservation_status_set

        out["capacity_reservation_statuses"] = (
            aws_sdk_ec2.types.capacity_reservation_status_set.deserialize_ec2_query(
                el, "CapacityReservationStatusSet"
            )
        )
    return out
