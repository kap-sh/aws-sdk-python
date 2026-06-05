"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_block_extension_status
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class CapacityBlockExtension(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The reservation ID of the Capacity Block extension.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block extension.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block extension.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the Capacity Block extension.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID of the Capacity Block extension.</p>"""
    capacity_block_extension_offering_id: NotRequired[
        "aws_sdk_ec2.types.offering_id.OfferingId"
    ]
    """<p>The ID of the Capacity Block extension offering.</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The duration of the Capacity Block extension in hours.</p>"""
    capacity_block_extension_status: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_status.CapacityBlockExtensionStatus"
    ]
    """<p>The status of the Capacity Block extension. A Capacity Block extension can have one of the following statuses:</p> <ul> <li> <p> <code>payment-pending</code> - The Capacity Block extension payment is processing. If your payment can't be processed within 12 hours, the Capacity Block extension is failed.</p> </li> <li> <p> <code>payment-failed</code> - Payment for the Capacity Block extension request was not successful.</p> </li> <li> <p> <code>payment-succeeded</code> - Payment for the Capacity Block extension request was successful. You receive an invoice that reflects the one-time upfront payment. In the invoice, you can associate the paid amount with the Capacity Block reservation ID.</p> </li> </ul>"""
    capacity_block_extension_purchase_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date when the Capacity Block extension was purchased.</p>"""
    capacity_block_extension_start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date of the Capacity Block extension.</p>"""
    capacity_block_extension_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The end date of the Capacity Block extension.</p>"""
    upfront_fee: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total price to be paid up front.</p>"""
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block extension.</p>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block extension is located.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockExtension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
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
    if "capacity_block_extension_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockExtensionOfferingId",
                str(value["capacity_block_extension_offering_id"]),
            )
        )
    if "capacity_block_extension_duration_hours" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockExtensionDurationHours",
                str(value["capacity_block_extension_duration_hours"]),
            )
        )
    if "capacity_block_extension_status" in value:
        import aws_sdk_ec2.types.capacity_block_extension_status

        aws_sdk_ec2.types.capacity_block_extension_status.serialize_ec2_query(
            value["capacity_block_extension_status"],
            pairs,
            f"{prefix}.CapacityBlockExtensionStatus",
        )
    if "capacity_block_extension_purchase_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["capacity_block_extension_purchase_date"],
            pairs,
            f"{prefix}.CapacityBlockExtensionPurchaseDate",
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
    if "upfront_fee" in value:
        pairs.append((f"{prefix}.UpfrontFee", str(value["upfront_fee"])))
    if "currency_code" in value:
        pairs.append((f"{prefix}.CurrencyCode", str(value["currency_code"])))
    if "zone_type" in value:
        pairs.append((f"{prefix}.ZoneType", str(value["zone_type"])))


def deserialize_ec2_query(el: Element) -> CapacityBlockExtension:
    out: CapacityBlockExtension = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
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
    child_capacity_block_extension_offering_id = el.find(
        "CapacityBlockExtensionOfferingId"
    )
    if child_capacity_block_extension_offering_id is not None:
        out["capacity_block_extension_offering_id"] = str(
            child_capacity_block_extension_offering_id.text or ""
        )
    child_capacity_block_extension_duration_hours = el.find(
        "CapacityBlockExtensionDurationHours"
    )
    if child_capacity_block_extension_duration_hours is not None:
        out["capacity_block_extension_duration_hours"] = int(
            child_capacity_block_extension_duration_hours.text or ""
        )
    child_capacity_block_extension_status = el.find("CapacityBlockExtensionStatus")
    if child_capacity_block_extension_status is not None:
        import aws_sdk_ec2.types.capacity_block_extension_status

        out["capacity_block_extension_status"] = (
            aws_sdk_ec2.types.capacity_block_extension_status.deserialize_ec2_query(
                child_capacity_block_extension_status
            )
        )
    child_capacity_block_extension_purchase_date = el.find(
        "CapacityBlockExtensionPurchaseDate"
    )
    if child_capacity_block_extension_purchase_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["capacity_block_extension_purchase_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_capacity_block_extension_purchase_date
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
    child_upfront_fee = el.find("UpfrontFee")
    if child_upfront_fee is not None:
        out["upfront_fee"] = str(child_upfront_fee.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_zone_type = el.find("ZoneType")
    if child_zone_type is not None:
        out["zone_type"] = str(child_zone_type.text or "")
    return out
