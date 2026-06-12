"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#StartNextPendingJobExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.details_map
    import aws_sdk_iot_jobs_data_plane.types.step_timeout_in_minutes
    import aws_sdk_iot_jobs_data_plane.types.thing_name


class StartNextPendingJobExecutionRequest(TypedDict):
    thing_name: "aws_sdk_iot_jobs_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing associated with the device.</p>"""
    status_details: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.details_map.DetailsMap"
    ]
    """<p>A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>"""
    step_timeout_in_minutes: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.step_timeout_in_minutes.StepTimeoutInMinutes"
    ]
    """<p>Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling <code>UpdateJobExecution</code>, setting the status to <code>IN_PROGRESS</code>, and specifying a new timeout value in field <code>stepTimeoutInMinutes</code>) the job execution status will be automatically set to <code>TIMED_OUT</code>. Note that setting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (<code>CreateJob</code> using field <code>timeoutConfig</code>).</p> <p>Valid values for this parameter range from 1 to 10080 (1 minute to 7 days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNextPendingJobExecutionRequest) -> dict:
    out: dict = {}
    if "status_details" in value:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["statusDetails"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.serialize_json(
                value["status_details"]
            )
        )
    if "step_timeout_in_minutes" in value:
        out["stepTimeoutInMinutes"] = value["step_timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> StartNextPendingJobExecutionRequest:
    out: StartNextPendingJobExecutionRequest = {}  # type: ignore[typeddict-item]
    if "statusDetails" in data:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["status_details"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.deserialize_json(
                data["statusDetails"]
            )
        )
    if "stepTimeoutInMinutes" in data:
        out["step_timeout_in_minutes"] = data["stepTimeoutInMinutes"]
    return out
