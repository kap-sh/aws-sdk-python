"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyRetainRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.interval
    import capo_dlm.types.retention_interval_unit_values


class CrossRegionCopyRetainRule(TypedDict, closed=True):
    interval: NotRequired["capo_dlm.types.interval.Interval"]
    """<p>The amount of time to retain a cross-Region snapshot or AMI copy. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.</p>"""
    interval_unit: NotRequired[
        "capo_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time for time-based retention. For example, to retain a cross-Region copy for 3 months, specify <code>Interval=3</code> and <code>IntervalUnit=MONTHS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyRetainRule) -> dict:
    out: dict = {}
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "interval_unit" in value:
        import capo_dlm.types.retention_interval_unit_values

        out["IntervalUnit"] = (
            capo_dlm.types.retention_interval_unit_values.serialize_json(
                value["interval_unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrossRegionCopyRetainRule:
    out: CrossRegionCopyRetainRule = {}  # type: ignore[typeddict-item]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "IntervalUnit" in data:
        import capo_dlm.types.retention_interval_unit_values

        out["interval_unit"] = (
            capo_dlm.types.retention_interval_unit_values.deserialize_json(
                data["IntervalUnit"]
            )
        )
    return out
