"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#StartNextPendingJobExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.job_execution


class StartNextPendingJobExecutionResponse(TypedDict, closed=True):
    execution: NotRequired["capo_iot_jobs_data_plane.types.job_execution.JobExecution"]
    """<p>A JobExecution object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNextPendingJobExecutionResponse) -> dict:
    out: dict = {}
    if "execution" in value:
        import capo_iot_jobs_data_plane.types.job_execution

        out["execution"] = capo_iot_jobs_data_plane.types.job_execution.serialize_json(
            value["execution"]
        )
    return out


def deserialize_json(data: dict) -> StartNextPendingJobExecutionResponse:
    out: StartNextPendingJobExecutionResponse = {}  # type: ignore[typeddict-item]
    if "execution" in data:
        import capo_iot_jobs_data_plane.types.job_execution

        out["execution"] = (
            capo_iot_jobs_data_plane.types.job_execution.deserialize_json(
                data["execution"]
            )
        )
    return out
