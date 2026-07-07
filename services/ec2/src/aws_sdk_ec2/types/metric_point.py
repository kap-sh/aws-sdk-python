"""Generated from Smithy shape ``com.amazonaws.ec2#MetricPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.float
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class MetricPoint(TypedDict, closed=True):
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date for the metric point. The starting date for the metric point. The starting time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-10T12:00:00.000Z</code>.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date for the metric point. The ending time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-12T12:00:00.000Z</code>.</p>"""
    value: NotRequired["aws_sdk_ec2.types.float.Float"]
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the metric point.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricPoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "start_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "end_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_ec2_query(el: Element) -> MetricPoint:
    out: MetricPoint = {}  # type: ignore[typeddict-item]
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_date
            )
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["end_date"] = aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = float(child_value.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
