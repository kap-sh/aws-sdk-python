"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#TimePeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime


class TimePeriod(TypedDict):
    start_time_inclusive: NotRequired["datetime.datetime"]
    """<p>The start time of the period, inclusive. Events at or after this time are included.</p>"""
    end_time_exclusive: NotRequired["datetime.datetime"]
    """<p>The end time of the period, exclusive. Events before this time are included.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriod) -> dict:
    out: dict = {}
    if "start_time_inclusive" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["startTimeInclusive"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_time_inclusive"]
            )
        )
    if "end_time_exclusive" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["endTimeExclusive"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time_exclusive"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "startTimeInclusive" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["start_time_inclusive"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTimeInclusive"]
            )
        )
    if "endTimeExclusive" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["end_time_exclusive"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTimeExclusive"]
            )
        )
    return out
