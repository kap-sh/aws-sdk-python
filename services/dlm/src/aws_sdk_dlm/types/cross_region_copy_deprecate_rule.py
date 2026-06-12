"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyDeprecateRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.interval
    import aws_sdk_dlm.types.retention_interval_unit_values


class CrossRegionCopyDeprecateRule(TypedDict):
    interval: NotRequired["aws_sdk_dlm.types.interval.Interval"]
    """<p>The period after which to deprecate the cross-Region AMI copies. The period must be less than or equal to the cross-Region AMI copy retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.</p>"""
    interval_unit: NotRequired[
        "aws_sdk_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time in which to measure the <b>Interval</b>. For example, to deprecate a cross-Region AMI copy after 3 months, specify <code>Interval=3</code> and <code>IntervalUnit=MONTHS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyDeprecateRule) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CrossRegionCopyDeprecateRule:
    out: CrossRegionCopyDeprecateRule = {}  # type: ignore[typeddict-item]
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
