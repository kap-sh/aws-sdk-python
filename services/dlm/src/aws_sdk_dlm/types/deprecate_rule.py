"""Generated from Smithy shape ``com.amazonaws.dlm#DeprecateRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.count
    import aws_sdk_dlm.types.interval
    import aws_sdk_dlm.types.retention_interval_unit_values


class DeprecateRule(TypedDict, closed=True):
    count: NotRequired["aws_sdk_dlm.types.count.Count"]
    """<p>If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate. The count must be less than or equal to the schedule's retention count, and it can't be greater than 1000.</p>"""
    interval: NotRequired["aws_sdk_dlm.types.interval.Interval"]
    """<p>If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule. The period must be less than or equal to the schedule's retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.</p>"""
    interval_unit: NotRequired[
        "aws_sdk_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time in which to measure the <b>Interval</b>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecateRule) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "interval_unit" in value:
        import aws_sdk_dlm.types.retention_interval_unit_values

        out["IntervalUnit"] = (
            aws_sdk_dlm.types.retention_interval_unit_values.serialize_json(
                value["interval_unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeprecateRule:
    out: DeprecateRule = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "IntervalUnit" in data:
        import aws_sdk_dlm.types.retention_interval_unit_values

        out["interval_unit"] = (
            aws_sdk_dlm.types.retention_interval_unit_values.deserialize_json(
                data["IntervalUnit"]
            )
        )
    return out
