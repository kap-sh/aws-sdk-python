"""Generated from Smithy shape ``com.amazonaws.iot#StatisticalThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.evaluation_statistic


class StatisticalThreshold(TypedDict, closed=True):
    statistic: NotRequired["aws_sdk_iot.types.evaluation_statistic.EvaluationStatistic"]
    """<p>The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (<code>durationSeconds</code>) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (<code>comparisonOperator</code>) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticalThreshold) -> dict:
    out: dict = {}
    if "statistic" in value:
        out["statistic"] = value["statistic"]
    return out


def deserialize_json(data: dict) -> StatisticalThreshold:
    out: StatisticalThreshold = {}  # type: ignore[typeddict-item]
    if "statistic" in data:
        out["statistic"] = data["statistic"]
    return out
