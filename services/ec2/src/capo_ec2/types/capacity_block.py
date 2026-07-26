"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_id
    import capo_ec2.types.capacity_block_resource_state
    import capo_ec2.types.capacity_reservation_id_set
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class CapacityBlock(TypedDict, closed=True):
    capacity_block_id: NotRequired["capo_ec2.types.capacity_block_id.CapacityBlockId"]
    """<p>The ID of the Capacity Block.</p>"""
    ultraserver_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the Capacity Block.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone ID of the Capacity Block.</p>"""
    capacity_reservation_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Block was started.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Block expires. When a Capacity Block expires, all instances in the Capacity Block are terminated.</p>"""
    create_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Block was created.</p>"""
    state: NotRequired[
        "capo_ec2.types.capacity_block_resource_state.CapacityBlockResourceState"
    ]
    """<p>The state of the Capacity Block.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Capacity Block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlock, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_block_id" in value:
        pairs.append((f"{prefix}.CapacityBlockId", str(value["capacity_block_id"])))
    if "ultraserver_type" in value:
        pairs.append((f"{prefix}.UltraserverType", str(value["ultraserver_type"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "capacity_reservation_ids" in value:
        import capo_ec2.types.capacity_reservation_id_set

        capo_ec2.types.capacity_reservation_id_set.serialize_ec2_query(
            value["capacity_reservation_ids"],
            pairs,
            f"{prefix}.CapacityReservationIdSet",
        )
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "create_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "state" in value:
        import capo_ec2.types.capacity_block_resource_state

        capo_ec2.types.capacity_block_resource_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> CapacityBlock:
    out: CapacityBlock = {}  # type: ignore[typeddict-item]
    child_capacity_block_id = el.find("CapacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_ultraserver_type = el.find("UltraserverType")
    if child_ultraserver_type is not None:
        out["ultraserver_type"] = str(child_ultraserver_type.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    if el.find("CapacityReservationIdSet") is not None:
        import capo_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            capo_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                el, "CapacityReservationIdSet"
            )
        )
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_date
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.capacity_block_resource_state

        out["state"] = (
            capo_ec2.types.capacity_block_resource_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
