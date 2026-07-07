"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_recurrence
    import aws_sdk_ec2.types.string


class ScheduledInstance(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date when the Scheduled Instance was purchased.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price for a single instance.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    network_platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network platform.</p>"""
    next_slot_start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time for the next schedule to start.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p>"""
    previous_slot_end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the previous schedule ended or will end.</p>"""
    recurrence: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_recurrence.ScheduledInstanceRecurrence"
    ]
    """<p>The schedule recurrence.</p>"""
    scheduled_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Scheduled Instance ID.</p>"""
    slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of hours in the schedule.</p>"""
    term_end_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date for the Scheduled Instance.</p>"""
    term_start_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date for the Scheduled Instance.</p>"""
    total_scheduled_instance_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of hours for a single instance for the entire term.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "create_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "hourly_price" in value:
        pairs.append((f"{prefix}.HourlyPrice", str(value["hourly_price"])))
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "network_platform" in value:
        pairs.append((f"{prefix}.NetworkPlatform", str(value["network_platform"])))
    if "next_slot_start_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["next_slot_start_time"], pairs, f"{prefix}.NextSlotStartTime"
        )
    if "platform" in value:
        pairs.append((f"{prefix}.Platform", str(value["platform"])))
    if "previous_slot_end_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["previous_slot_end_time"], pairs, f"{prefix}.PreviousSlotEndTime"
        )
    if "recurrence" in value:
        import aws_sdk_ec2.types.scheduled_instance_recurrence

        aws_sdk_ec2.types.scheduled_instance_recurrence.serialize_ec2_query(
            value["recurrence"], pairs, f"{prefix}.Recurrence"
        )
    if "scheduled_instance_id" in value:
        pairs.append(
            (f"{prefix}.ScheduledInstanceId", str(value["scheduled_instance_id"]))
        )
    if "slot_duration_in_hours" in value:
        pairs.append(
            (f"{prefix}.SlotDurationInHours", str(value["slot_duration_in_hours"]))
        )
    if "term_end_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["term_end_date"], pairs, f"{prefix}.TermEndDate"
        )
    if "term_start_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["term_start_date"], pairs, f"{prefix}.TermStartDate"
        )
    if "total_scheduled_instance_hours" in value:
        pairs.append(
            (
                f"{prefix}.TotalScheduledInstanceHours",
                str(value["total_scheduled_instance_hours"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ScheduledInstance:
    out: ScheduledInstance = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_ec2.types.date_time

        out["create_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    child_hourly_price = el.find("HourlyPrice")
    if child_hourly_price is not None:
        out["hourly_price"] = str(child_hourly_price.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_network_platform = el.find("NetworkPlatform")
    if child_network_platform is not None:
        out["network_platform"] = str(child_network_platform.text or "")
    child_next_slot_start_time = el.find("NextSlotStartTime")
    if child_next_slot_start_time is not None:
        import aws_sdk_ec2.types.date_time

        out["next_slot_start_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_next_slot_start_time
        )
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_previous_slot_end_time = el.find("PreviousSlotEndTime")
    if child_previous_slot_end_time is not None:
        import aws_sdk_ec2.types.date_time

        out["previous_slot_end_time"] = (
            aws_sdk_ec2.types.date_time.deserialize_ec2_query(
                child_previous_slot_end_time
            )
        )
    child_recurrence = el.find("Recurrence")
    if child_recurrence is not None:
        import aws_sdk_ec2.types.scheduled_instance_recurrence

        out["recurrence"] = (
            aws_sdk_ec2.types.scheduled_instance_recurrence.deserialize_ec2_query(
                child_recurrence
            )
        )
    child_scheduled_instance_id = el.find("ScheduledInstanceId")
    if child_scheduled_instance_id is not None:
        out["scheduled_instance_id"] = str(child_scheduled_instance_id.text or "")
    child_slot_duration_in_hours = el.find("SlotDurationInHours")
    if child_slot_duration_in_hours is not None:
        out["slot_duration_in_hours"] = int(child_slot_duration_in_hours.text or "")
    child_term_end_date = el.find("TermEndDate")
    if child_term_end_date is not None:
        import aws_sdk_ec2.types.date_time

        out["term_end_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_term_end_date
        )
    child_term_start_date = el.find("TermStartDate")
    if child_term_start_date is not None:
        import aws_sdk_ec2.types.date_time

        out["term_start_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_term_start_date
        )
    child_total_scheduled_instance_hours = el.find("TotalScheduledInstanceHours")
    if child_total_scheduled_instance_hours is not None:
        out["total_scheduled_instance_hours"] = int(
            child_total_scheduled_instance_hours.text or ""
        )
    return out
