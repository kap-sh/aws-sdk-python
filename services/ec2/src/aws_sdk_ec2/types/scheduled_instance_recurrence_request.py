"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceRecurrenceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.occurrence_day_request_set
    import aws_sdk_ec2.types.string


class ScheduledInstanceRecurrenceRequest(TypedDict):
    frequency: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The frequency (<code>Daily</code>, <code>Weekly</code>, or <code>Monthly</code>).</p>"""
    interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The interval quantity. The interval unit depends on the value of <code>Frequency</code>. For example, every 2 weeks or every 2 months.</p>"""
    occurrence_days: NotRequired[
        "aws_sdk_ec2.types.occurrence_day_request_set.OccurrenceDayRequestSet"
    ]
    """<p>The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can't specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.</p>"""
    occurrence_relative_to_end: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.</p>"""
    occurrence_unit: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The unit for <code>OccurrenceDays</code> (<code>DayOfWeek</code> or <code>DayOfMonth</code>). This value is required for a monthly schedule. You can't specify <code>DayOfWeek</code> with a weekly schedule. You can't specify this value with a daily schedule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceRecurrenceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "frequency" in value:
        pairs.append((f"{prefix}.Frequency", str(value["frequency"])))
    if "interval" in value:
        pairs.append((f"{prefix}.Interval", str(value["interval"])))
    if "occurrence_days" in value:
        import aws_sdk_ec2.types.occurrence_day_request_set

        aws_sdk_ec2.types.occurrence_day_request_set.serialize_ec2_query(
            value["occurrence_days"], pairs, f"{prefix}.OccurrenceDays"
        )
    if "occurrence_relative_to_end" in value:
        pairs.append(
            (
                f"{prefix}.OccurrenceRelativeToEnd",
                "true" if value["occurrence_relative_to_end"] else "false",
            )
        )
    if "occurrence_unit" in value:
        pairs.append((f"{prefix}.OccurrenceUnit", str(value["occurrence_unit"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstanceRecurrenceRequest:
    out: ScheduledInstanceRecurrenceRequest = {}  # type: ignore[typeddict-item]
    child_frequency = el.find("Frequency")
    if child_frequency is not None:
        out["frequency"] = str(child_frequency.text or "")
    child_interval = el.find("Interval")
    if child_interval is not None:
        out["interval"] = int(child_interval.text or "")
    if el.find("OccurrenceDays") is not None:
        import aws_sdk_ec2.types.occurrence_day_request_set

        out["occurrence_days"] = (
            aws_sdk_ec2.types.occurrence_day_request_set.deserialize_ec2_query(
                el, "OccurrenceDays"
            )
        )
    child_occurrence_relative_to_end = el.find("OccurrenceRelativeToEnd")
    if child_occurrence_relative_to_end is not None:
        out["occurrence_relative_to_end"] = (
            child_occurrence_relative_to_end.text or ""
        ).lower() == "true"
    child_occurrence_unit = el.find("OccurrenceUnit")
    if child_occurrence_unit is not None:
        out["occurrence_unit"] = str(child_occurrence_unit.text or "")
    return out
