"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunTimeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.timestamp


class CanaryRunTimeline(TypedDict, closed=True):
    started: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The start time of the run.</p>"""
    completed: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The end time of the run.</p>"""
    metric_timestamp_for_run_and_retries: NotRequired[
        "capo_synthetics.types.timestamp.Timestamp"
    ]
    """<p>The time at which the metrics will be generated for this run or retries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunTimeline) -> dict:
    out: dict = {}
    if "started" in value:
        import capo_synthetics.types.timestamp

        out["Started"] = capo_synthetics.types.timestamp.serialize_json(
            value["started"]
        )
    if "completed" in value:
        import capo_synthetics.types.timestamp

        out["Completed"] = capo_synthetics.types.timestamp.serialize_json(
            value["completed"]
        )
    if "metric_timestamp_for_run_and_retries" in value:
        import capo_synthetics.types.timestamp

        out["MetricTimestampForRunAndRetries"] = (
            capo_synthetics.types.timestamp.serialize_json(
                value["metric_timestamp_for_run_and_retries"]
            )
        )
    return out


def deserialize_json(data: dict) -> CanaryRunTimeline:
    out: CanaryRunTimeline = {}  # type: ignore[typeddict-item]
    if "Started" in data:
        import capo_synthetics.types.timestamp

        out["started"] = capo_synthetics.types.timestamp.deserialize_json(
            data["Started"]
        )
    if "Completed" in data:
        import capo_synthetics.types.timestamp

        out["completed"] = capo_synthetics.types.timestamp.deserialize_json(
            data["Completed"]
        )
    if "MetricTimestampForRunAndRetries" in data:
        import capo_synthetics.types.timestamp

        out["metric_timestamp_for_run_and_retries"] = (
            capo_synthetics.types.timestamp.deserialize_json(
                data["MetricTimestampForRunAndRetries"]
            )
        )
    return out
