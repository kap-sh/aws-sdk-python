"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunTimeline``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.timestamp


class CanaryRunTimeline(TypedDict):
    started: NotRequired["aws_sdk_synthetics.types.timestamp.Timestamp"]
    """<p>The start time of the run.</p>"""
    completed: NotRequired["aws_sdk_synthetics.types.timestamp.Timestamp"]
    """<p>The end time of the run.</p>"""
    metric_timestamp_for_run_and_retries: NotRequired[
        "aws_sdk_synthetics.types.timestamp.Timestamp"
    ]
    """<p>The time at which the metrics will be generated for this run or retries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunTimeline) -> dict:
    out: dict = {}
    if "started" in value:
        import aws_sdk_synthetics.types.timestamp

        out["Started"] = aws_sdk_synthetics.types.timestamp.serialize_json(
            value["started"]
        )
    if "completed" in value:
        import aws_sdk_synthetics.types.timestamp

        out["Completed"] = aws_sdk_synthetics.types.timestamp.serialize_json(
            value["completed"]
        )
    if "metric_timestamp_for_run_and_retries" in value:
        import aws_sdk_synthetics.types.timestamp

        out["MetricTimestampForRunAndRetries"] = (
            aws_sdk_synthetics.types.timestamp.serialize_json(
                value["metric_timestamp_for_run_and_retries"]
            )
        )
    return out


def deserialize_json(data: dict) -> CanaryRunTimeline:
    out: CanaryRunTimeline = {}  # type: ignore[typeddict-item]
    if "Started" in data:
        import aws_sdk_synthetics.types.timestamp

        out["started"] = aws_sdk_synthetics.types.timestamp.deserialize_json(
            data["Started"]
        )
    if "Completed" in data:
        import aws_sdk_synthetics.types.timestamp

        out["completed"] = aws_sdk_synthetics.types.timestamp.deserialize_json(
            data["Completed"]
        )
    if "MetricTimestampForRunAndRetries" in data:
        import aws_sdk_synthetics.types.timestamp

        out["metric_timestamp_for_run_and_retries"] = (
            aws_sdk_synthetics.types.timestamp.deserialize_json(
                data["MetricTimestampForRunAndRetries"]
            )
        )
    return out
