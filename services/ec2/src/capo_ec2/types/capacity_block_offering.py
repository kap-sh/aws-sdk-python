"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.capacity_reservation_tenancy
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.offering_id
    import capo_ec2.types.string


class CapacityBlockOffering(TypedDict, closed=True):
    capacity_block_offering_id: NotRequired["capo_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the Capacity Block offering.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block offering.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the Capacity Block offering.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block offering.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The start date of the Capacity Block offering.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date of the Capacity Block offering.</p>"""
    capacity_block_duration_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of hours (in addition to <code>capacityBlockDurationMinutes</code>) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at <b>04:55</b> and ends at <b>11:30</b>, the hours field would be <b>6</b>.</p>"""
    upfront_fee: NotRequired["capo_ec2.types.string.String"]
    """<p>The total price to be paid up front.</p>"""
    currency_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block.</p>"""
    tenancy: NotRequired[
        "capo_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>The tenancy of the Capacity Block.</p>"""
    ultraserver_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block offering.</p>"""
    ultraserver_count: NotRequired["capo_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The number of EC2 UltraServers in the offering.</p>"""
    capacity_block_duration_minutes: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of minutes (in addition to <code>capacityBlockDurationHours</code>) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at <b>08:55</b> and ends at <b>11:30</b>, the minutes field would be <b>35</b>.</p>"""
    zone_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block offering is available.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_block_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockOfferingId",
                str(value["capacity_block_offering_id"]),
            )
        )
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
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
    if "capacity_block_duration_hours" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockDurationHours",
                str(value["capacity_block_duration_hours"]),
            )
        )
    if "upfront_fee" in value:
        pairs.append((f"{prefix}.UpfrontFee", str(value["upfront_fee"])))
    if "currency_code" in value:
        pairs.append((f"{prefix}.CurrencyCode", str(value["currency_code"])))
    if "tenancy" in value:
        import capo_ec2.types.capacity_reservation_tenancy

        capo_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "ultraserver_type" in value:
        pairs.append((f"{prefix}.UltraserverType", str(value["ultraserver_type"])))
    if "ultraserver_count" in value:
        pairs.append((f"{prefix}.UltraserverCount", str(value["ultraserver_count"])))
    if "capacity_block_duration_minutes" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockDurationMinutes",
                str(value["capacity_block_duration_minutes"]),
            )
        )
    if "zone_type" in value:
        pairs.append((f"{prefix}.ZoneType", str(value["zone_type"])))


def deserialize_ec2_query(el: Element) -> CapacityBlockOffering:
    out: CapacityBlockOffering = {}  # type: ignore[typeddict-item]
    child_capacity_block_offering_id = el.find("CapacityBlockOfferingId")
    if child_capacity_block_offering_id is not None:
        out["capacity_block_offering_id"] = str(
            child_capacity_block_offering_id.text or ""
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
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
    child_capacity_block_duration_hours = el.find("CapacityBlockDurationHours")
    if child_capacity_block_duration_hours is not None:
        out["capacity_block_duration_hours"] = int(
            child_capacity_block_duration_hours.text or ""
        )
    child_upfront_fee = el.find("UpfrontFee")
    if child_upfront_fee is not None:
        out["upfront_fee"] = str(child_upfront_fee.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            capo_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_ultraserver_type = el.find("UltraserverType")
    if child_ultraserver_type is not None:
        out["ultraserver_type"] = str(child_ultraserver_type.text or "")
    child_ultraserver_count = el.find("UltraserverCount")
    if child_ultraserver_count is not None:
        out["ultraserver_count"] = int(child_ultraserver_count.text or "")
    child_capacity_block_duration_minutes = el.find("CapacityBlockDurationMinutes")
    if child_capacity_block_duration_minutes is not None:
        out["capacity_block_duration_minutes"] = int(
            child_capacity_block_duration_minutes.text or ""
        )
    child_zone_type = el.find("ZoneType")
    if child_zone_type is not None:
        out["zone_type"] = str(child_zone_type.text or "")
    return out
