"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtensionOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class CapacityBlockExtensionOffering(TypedDict):
    capacity_block_extension_offering_id: NotRequired[
        "aws_sdk_ec2.types.offering_id.OfferingId"
    ]
    """<p>The ID of the Capacity Block extension offering.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block that will be extended.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block extension offering.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the Capacity Block that will be extended.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID of the Capacity Block that will be extended.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date of the Capacity Block that will be extended.</p>"""
    capacity_block_extension_start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block extension will start. This date is also the same as the end date of the Capacity Block that will be extended.</p>"""
    capacity_block_extension_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block extension expires. When a Capacity Block expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Block's state changes to <code>expired</code> when it reaches its end date</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The amount of time of the Capacity Block extension offering in hours.</p>"""
    upfront_fee: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total price of the Capacity Block extension offering, to be paid up front.</p>"""
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block extension offering.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Block extension offering. A Capacity Block can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Block is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Block is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block extension offering is available.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockExtensionOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_block_extension_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockExtensionOfferingId",
                str(value["capacity_block_extension_offering_id"]),
            )
        )
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "start_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "capacity_block_extension_start_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["capacity_block_extension_start_date"],
            pairs,
            f"{prefix}.CapacityBlockExtensionStartDate",
        )
    if "capacity_block_extension_end_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["capacity_block_extension_end_date"],
            pairs,
            f"{prefix}.CapacityBlockExtensionEndDate",
        )
    if "capacity_block_extension_duration_hours" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockExtensionDurationHours",
                str(value["capacity_block_extension_duration_hours"]),
            )
        )
    if "upfront_fee" in value:
        pairs.append((f"{prefix}.UpfrontFee", str(value["upfront_fee"])))
    if "currency_code" in value:
        pairs.append((f"{prefix}.CurrencyCode", str(value["currency_code"])))
    if "tenancy" in value:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        aws_sdk_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "zone_type" in value:
        pairs.append((f"{prefix}.ZoneType", str(value["zone_type"])))


def deserialize_ec2_query(el: Element) -> CapacityBlockExtensionOffering:
    out: CapacityBlockExtensionOffering = {}  # type: ignore[typeddict-item]
    child_capacity_block_extension_offering_id = el.find(
        "CapacityBlockExtensionOfferingId"
    )
    if child_capacity_block_extension_offering_id is not None:
        out["capacity_block_extension_offering_id"] = str(
            child_capacity_block_extension_offering_id.text or ""
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_date
            )
        )
    child_capacity_block_extension_start_date = el.find(
        "CapacityBlockExtensionStartDate"
    )
    if child_capacity_block_extension_start_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["capacity_block_extension_start_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_capacity_block_extension_start_date
            )
        )
    child_capacity_block_extension_end_date = el.find("CapacityBlockExtensionEndDate")
    if child_capacity_block_extension_end_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["capacity_block_extension_end_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_capacity_block_extension_end_date
            )
        )
    child_capacity_block_extension_duration_hours = el.find(
        "CapacityBlockExtensionDurationHours"
    )
    if child_capacity_block_extension_duration_hours is not None:
        out["capacity_block_extension_duration_hours"] = int(
            child_capacity_block_extension_duration_hours.text or ""
        )
    child_upfront_fee = el.find("UpfrontFee")
    if child_upfront_fee is not None:
        out["upfront_fee"] = str(child_upfront_fee.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            aws_sdk_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_zone_type = el.find("ZoneType")
    if child_zone_type is not None:
        out["zone_type"] = str(child_zone_type.text or "")
    return out
