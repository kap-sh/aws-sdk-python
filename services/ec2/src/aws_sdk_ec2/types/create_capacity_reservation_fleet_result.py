"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationFleetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_id
    import aws_sdk_ec2.types.capacity_reservation_fleet_state
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.fleet_capacity_reservation_set
    import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy
    import aws_sdk_ec2.types.fleet_instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CreateCapacityReservationFleetResult(TypedDict):
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The status of the Capacity Reservation Fleet.</p>"""
    total_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of capacity units for which the Capacity Reservation Fleet reserves capacity.</p>"""
    total_fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The requested capacity units that have been successfully reserved.</p>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
    ]
    """<p>The instance matching criteria for the Capacity Reservation Fleet.</p>"""
    allocation_strategy: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation strategy used by the Capacity Reservation Fleet.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Reservation Fleet was created.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of Capacity Reservation Fleet.</p>"""
    fleet_capacity_reservations: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_set.FleetCapacityReservationSet"
    ]
    """<p>Information about the individual Capacity Reservations in the Capacity Reservation Fleet.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Capacity Reservation Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationFleetResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )
    if "state" in value:
        import aws_sdk_ec2.types.capacity_reservation_fleet_state

        aws_sdk_ec2.types.capacity_reservation_fleet_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "total_target_capacity" in value:
        pairs.append(
            (f"{prefix}.TotalTargetCapacity", str(value["total_target_capacity"]))
        )
    if "total_fulfilled_capacity" in value:
        pairs.append(
            (f"{prefix}.TotalFulfilledCapacity", str(value["total_fulfilled_capacity"]))
        )
    if "instance_match_criteria" in value:
        import aws_sdk_ec2.types.fleet_instance_match_criteria

        aws_sdk_ec2.types.fleet_instance_match_criteria.serialize_ec2_query(
            value["instance_match_criteria"], pairs, f"{prefix}.InstanceMatchCriteria"
        )
    if "allocation_strategy" in value:
        pairs.append(
            (f"{prefix}.AllocationStrategy", str(value["allocation_strategy"]))
        )
    if "create_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "end_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "tenancy" in value:
        import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy

        aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "fleet_capacity_reservations" in value:
        import aws_sdk_ec2.types.fleet_capacity_reservation_set

        aws_sdk_ec2.types.fleet_capacity_reservation_set.serialize_ec2_query(
            value["fleet_capacity_reservations"],
            pairs,
            f"{prefix}.FleetCapacityReservationSet",
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationFleetResult:
    out: CreateCapacityReservationFleetResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_fleet_id = el.find("CapacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.capacity_reservation_fleet_state

        out["state"] = (
            aws_sdk_ec2.types.capacity_reservation_fleet_state.deserialize_ec2_query(
                child_state
            )
        )
    child_total_target_capacity = el.find("TotalTargetCapacity")
    if child_total_target_capacity is not None:
        out["total_target_capacity"] = int(child_total_target_capacity.text or "")
    child_total_fulfilled_capacity = el.find("TotalFulfilledCapacity")
    if child_total_fulfilled_capacity is not None:
        out["total_fulfilled_capacity"] = float(
            child_total_fulfilled_capacity.text or ""
        )
    child_instance_match_criteria = el.find("InstanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import aws_sdk_ec2.types.fleet_instance_match_criteria

        out["instance_match_criteria"] = (
            aws_sdk_ec2.types.fleet_instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    child_allocation_strategy = el.find("AllocationStrategy")
    if child_allocation_strategy is not None:
        out["allocation_strategy"] = str(child_allocation_strategy.text or "")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["create_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_create_time
            )
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["end_date"] = aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy

        out["tenancy"] = (
            aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    if el.find("FleetCapacityReservationSet") is not None:
        import aws_sdk_ec2.types.fleet_capacity_reservation_set

        out["fleet_capacity_reservations"] = (
            aws_sdk_ec2.types.fleet_capacity_reservation_set.deserialize_ec2_query(
                el, "FleetCapacityReservationSet"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
