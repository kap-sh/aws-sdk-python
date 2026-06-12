"""Generated from Smithy shape ``com.amazonaws.glue#DQStopJobOnFailureOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.dq_stop_job_on_failure_timing


class DQStopJobOnFailureOptions(TypedDict):
    stop_job_on_failure_timing: NotRequired[
        "aws_sdk_glue.types.dq_stop_job_on_failure_timing.DQStopJobOnFailureTiming"
    ]
    """<p>When to stop job if your data quality evaluation fails. Options are Immediate or AfterDataLoad.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DQStopJobOnFailureOptions) -> dict:
    out: dict = {}
    if "stop_job_on_failure_timing" in value:
        import aws_sdk_glue.types.dq_stop_job_on_failure_timing

        out["StopJobOnFailureTiming"] = (
            aws_sdk_glue.types.dq_stop_job_on_failure_timing.serialize_aws_json_1_1(
                value["stop_job_on_failure_timing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DQStopJobOnFailureOptions:
    out: DQStopJobOnFailureOptions = {}  # type: ignore[typeddict-item]
    if "StopJobOnFailureTiming" in data:
        import aws_sdk_glue.types.dq_stop_job_on_failure_timing

        out["stop_job_on_failure_timing"] = (
            aws_sdk_glue.types.dq_stop_job_on_failure_timing.deserialize_aws_json_1_1(
                data["StopJobOnFailureTiming"]
            )
        )
    return out
