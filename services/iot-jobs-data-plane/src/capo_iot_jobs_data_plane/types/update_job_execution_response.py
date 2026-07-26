"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#UpdateJobExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.job_document
    import capo_iot_jobs_data_plane.types.job_execution_state


class UpdateJobExecutionResponse(TypedDict, closed=True):
    execution_state: NotRequired[
        "capo_iot_jobs_data_plane.types.job_execution_state.JobExecutionState"
    ]
    """<p>A JobExecutionState object.</p>"""
    job_document: NotRequired["capo_iot_jobs_data_plane.types.job_document.JobDocument"]
    """<p>The contents of the Job Documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobExecutionResponse) -> dict:
    out: dict = {}
    if "execution_state" in value:
        import capo_iot_jobs_data_plane.types.job_execution_state

        out["executionState"] = (
            capo_iot_jobs_data_plane.types.job_execution_state.serialize_json(
                value["execution_state"]
            )
        )
    if "job_document" in value:
        out["jobDocument"] = value["job_document"]
    return out


def deserialize_json(data: dict) -> UpdateJobExecutionResponse:
    out: UpdateJobExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionState" in data:
        import capo_iot_jobs_data_plane.types.job_execution_state

        out["execution_state"] = (
            capo_iot_jobs_data_plane.types.job_execution_state.deserialize_json(
                data["executionState"]
            )
        )
    if "jobDocument" in data:
        out["job_document"] = data["jobDocument"]
    return out
