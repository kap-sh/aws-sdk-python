"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceAvailability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.scheduled_instance_recurrence
    import capo_ec2.types.string


class ScheduledInstanceAvailability(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    available_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of available instances.</p>"""
    first_slot_start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time period for the first schedule to start.</p>"""
    hourly_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The hourly price for a single instance.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type. You can specify one of the C3, C4, M4, or R3 instance types.</p>"""
    max_term_duration_in_days: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum term. The only possible value is 365 days.</p>"""
    min_term_duration_in_days: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum term. The only possible value is 365 days.</p>"""
    network_platform: NotRequired["capo_ec2.types.string.String"]
    """<p>The network platform.</p>"""
    platform: NotRequired["capo_ec2.types.string.String"]
    """<p>The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p>"""
    purchase_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The purchase token. This token expires in two hours.</p>"""
    recurrence: NotRequired[
        "capo_ec2.types.scheduled_instance_recurrence.ScheduledInstanceRecurrence"
    ]
    """<p>The schedule recurrence.</p>"""
    slot_duration_in_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of hours in the schedule.</p>"""
    total_scheduled_instance_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of hours for a single instance for the entire term.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceAvailability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "available_instance_count" in value:
        pairs.append(
            (
                f"{key_prefix}AvailableInstanceCount",
                str(value["available_instance_count"]),
            )
        )
    if "first_slot_start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["first_slot_start_time"], pairs, f"{key_prefix}FirstSlotStartTime"
        )
    if "hourly_price" in value:
        pairs.append((f"{key_prefix}HourlyPrice", str(value["hourly_price"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "max_term_duration_in_days" in value:
        pairs.append(
            (
                f"{key_prefix}MaxTermDurationInDays",
                str(value["max_term_duration_in_days"]),
            )
        )
    if "min_term_duration_in_days" in value:
        pairs.append(
            (
                f"{key_prefix}MinTermDurationInDays",
                str(value["min_term_duration_in_days"]),
            )
        )
    if "network_platform" in value:
        pairs.append((f"{key_prefix}NetworkPlatform", str(value["network_platform"])))
    if "platform" in value:
        pairs.append((f"{key_prefix}Platform", str(value["platform"])))
    if "purchase_token" in value:
        pairs.append((f"{key_prefix}PurchaseToken", str(value["purchase_token"])))
    if "recurrence" in value:
        import capo_ec2.types.scheduled_instance_recurrence

        capo_ec2.types.scheduled_instance_recurrence.serialize_ec2_query(
            value["recurrence"], pairs, f"{key_prefix}Recurrence"
        )
    if "slot_duration_in_hours" in value:
        pairs.append(
            (f"{key_prefix}SlotDurationInHours", str(value["slot_duration_in_hours"]))
        )
    if "total_scheduled_instance_hours" in value:
        pairs.append(
            (
                f"{key_prefix}TotalScheduledInstanceHours",
                str(value["total_scheduled_instance_hours"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ScheduledInstanceAvailability:
    out: ScheduledInstanceAvailability = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_available_instance_count = el.find("AvailableInstanceCount")
    if child_available_instance_count is not None:
        out["available_instance_count"] = int(child_available_instance_count.text or "")
    child_first_slot_start_time = el.find("FirstSlotStartTime")
    if child_first_slot_start_time is not None:
        import capo_ec2.types.date_time

        out["first_slot_start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_first_slot_start_time
        )
    child_hourly_price = el.find("HourlyPrice")
    if child_hourly_price is not None:
        out["hourly_price"] = str(child_hourly_price.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_max_term_duration_in_days = el.find("MaxTermDurationInDays")
    if child_max_term_duration_in_days is not None:
        out["max_term_duration_in_days"] = int(
            child_max_term_duration_in_days.text or ""
        )
    child_min_term_duration_in_days = el.find("MinTermDurationInDays")
    if child_min_term_duration_in_days is not None:
        out["min_term_duration_in_days"] = int(
            child_min_term_duration_in_days.text or ""
        )
    child_network_platform = el.find("NetworkPlatform")
    if child_network_platform is not None:
        out["network_platform"] = str(child_network_platform.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_purchase_token = el.find("PurchaseToken")
    if child_purchase_token is not None:
        out["purchase_token"] = str(child_purchase_token.text or "")
    child_recurrence = el.find("Recurrence")
    if child_recurrence is not None:
        import capo_ec2.types.scheduled_instance_recurrence

        out["recurrence"] = (
            capo_ec2.types.scheduled_instance_recurrence.deserialize_ec2_query(
                child_recurrence
            )
        )
    child_slot_duration_in_hours = el.find("SlotDurationInHours")
    if child_slot_duration_in_hours is not None:
        out["slot_duration_in_hours"] = int(child_slot_duration_in_hours.text or "")
    child_total_scheduled_instance_hours = el.find("TotalScheduledInstanceHours")
    if child_total_scheduled_instance_hours is not None:
        out["total_scheduled_instance_hours"] = int(
            child_total_scheduled_instance_hours.text or ""
        )
    return out
