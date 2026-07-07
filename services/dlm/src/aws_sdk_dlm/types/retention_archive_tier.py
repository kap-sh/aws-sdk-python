"""Generated from Smithy shape ``com.amazonaws.dlm#RetentionArchiveTier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.count
    import aws_sdk_dlm.types.interval
    import aws_sdk_dlm.types.retention_interval_unit_values


class RetentionArchiveTier(TypedDict, closed=True):
    count: NotRequired["aws_sdk_dlm.types.count.Count"]
    """<p>The maximum number of snapshots to retain in the archive storage tier for each volume. The count must ensure that each snapshot remains in the archive tier for at least 90 days. For example, if the schedule creates snapshots every 30 days, you must specify a count of 3 or more to ensure that each snapshot is archived for at least 90 days.</p>"""
    interval: NotRequired["aws_sdk_dlm.types.interval.Interval"]
    """<p>Specifies the period of time to retain snapshots in the archive tier. After this period expires, the snapshot is permanently deleted.</p>"""
    interval_unit: NotRequired[
        "aws_sdk_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time in which to measure the <b>Interval</b>. For example, to retain a snapshots in the archive tier for 6 months, specify <code>Interval=6</code> and <code>IntervalUnit=MONTHS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetentionArchiveTier) -> dict:
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


def deserialize_json(data: dict) -> RetentionArchiveTier:
    out: RetentionArchiveTier = {}  # type: ignore[typeddict-item]
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
