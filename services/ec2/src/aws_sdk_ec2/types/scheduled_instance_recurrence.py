"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceRecurrence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.occurrence_day_set
    import aws_sdk_ec2.types.string


class ScheduledInstanceRecurrence(TypedDict, closed=True):
    frequency: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The frequency (<code>Daily</code>, <code>Weekly</code>, or <code>Monthly</code>).</p>"""
    interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The interval quantity. The interval unit depends on the value of <code>frequency</code>. For example, every 2 weeks or every 2 months.</p>"""
    occurrence_day_set: NotRequired[
        "aws_sdk_ec2.types.occurrence_day_set.OccurrenceDaySet"
    ]
    """<p>The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).</p>"""
    occurrence_relative_to_end: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the occurrence is relative to the end of the specified week or month.</p>"""
    occurrence_unit: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The unit for <code>occurrenceDaySet</code> (<code>DayOfWeek</code> or <code>DayOfMonth</code>).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceRecurrence, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "frequency" in value:
        pairs.append((f"{prefix}.Frequency", str(value["frequency"])))
    if "interval" in value:
        pairs.append((f"{prefix}.Interval", str(value["interval"])))
    if "occurrence_day_set" in value:
        import aws_sdk_ec2.types.occurrence_day_set

        aws_sdk_ec2.types.occurrence_day_set.serialize_ec2_query(
            value["occurrence_day_set"], pairs, f"{prefix}.OccurrenceDaySet"
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


def deserialize_ec2_query(el: Element) -> ScheduledInstanceRecurrence:
    out: ScheduledInstanceRecurrence = {}  # type: ignore[typeddict-item]
    child_frequency = el.find("Frequency")
    if child_frequency is not None:
        out["frequency"] = str(child_frequency.text or "")
    child_interval = el.find("Interval")
    if child_interval is not None:
        out["interval"] = int(child_interval.text or "")
    if el.find("OccurrenceDaySet") is not None:
        import aws_sdk_ec2.types.occurrence_day_set

        out["occurrence_day_set"] = (
            aws_sdk_ec2.types.occurrence_day_set.deserialize_ec2_query(
                el, "OccurrenceDaySet"
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
