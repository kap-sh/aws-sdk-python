"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.hour
    import aws_sdk_ec2.types.week_day


class InstanceEventWindowTimeRange(TypedDict):
    start_week_day: NotRequired["aws_sdk_ec2.types.week_day.WeekDay"]
    """<p>The day on which the time range begins.</p>"""
    start_hour: NotRequired["aws_sdk_ec2.types.hour.Hour"]
    """<p>The hour when the time range begins.</p>"""
    end_week_day: NotRequired["aws_sdk_ec2.types.week_day.WeekDay"]
    """<p>The day on which the time range ends.</p>"""
    end_hour: NotRequired["aws_sdk_ec2.types.hour.Hour"]
    """<p>The hour when the time range ends.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowTimeRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "start_week_day" in value:
        import aws_sdk_ec2.types.week_day

        aws_sdk_ec2.types.week_day.serialize_ec2_query(
            value["start_week_day"], pairs, f"{prefix}.StartWeekDay"
        )
    if "start_hour" in value:
        pairs.append((f"{prefix}.StartHour", str(value["start_hour"])))
    if "end_week_day" in value:
        import aws_sdk_ec2.types.week_day

        aws_sdk_ec2.types.week_day.serialize_ec2_query(
            value["end_week_day"], pairs, f"{prefix}.EndWeekDay"
        )
    if "end_hour" in value:
        pairs.append((f"{prefix}.EndHour", str(value["end_hour"])))


def deserialize_ec2_query(el: Element) -> InstanceEventWindowTimeRange:
    out: InstanceEventWindowTimeRange = {}  # type: ignore[typeddict-item]
    child_start_week_day = el.find("StartWeekDay")
    if child_start_week_day is not None:
        import aws_sdk_ec2.types.week_day

        out["start_week_day"] = aws_sdk_ec2.types.week_day.deserialize_ec2_query(
            child_start_week_day
        )
    child_start_hour = el.find("StartHour")
    if child_start_hour is not None:
        out["start_hour"] = int(child_start_hour.text or "")
    child_end_week_day = el.find("EndWeekDay")
    if child_end_week_day is not None:
        import aws_sdk_ec2.types.week_day

        out["end_week_day"] = aws_sdk_ec2.types.week_day.deserialize_ec2_query(
            child_end_week_day
        )
    child_end_hour = el.find("EndHour")
    if child_end_hour is not None:
        out["end_hour"] = int(child_end_hour.text or "")
    return out
