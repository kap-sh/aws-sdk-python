"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobRestartPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.batch_job_step_list


class ListBatchJobRestartPointsResponse(TypedDict, closed=True):
    batch_job_steps: NotRequired["capo_m2.types.batch_job_step_list.BatchJobStepList"]
    """<p>Returns all the batch job steps and related information for a batch job that previously ran.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobRestartPointsResponse) -> dict:
    out: dict = {}
    if "batch_job_steps" in value:
        import capo_m2.types.batch_job_step_list

        out["batchJobSteps"] = capo_m2.types.batch_job_step_list.serialize_json(
            value["batch_job_steps"]
        )
    return out


def deserialize_json(data: dict) -> ListBatchJobRestartPointsResponse:
    out: ListBatchJobRestartPointsResponse = {}  # type: ignore[typeddict-item]
    if "batchJobSteps" in data:
        import capo_m2.types.batch_job_step_list

        out["batch_job_steps"] = capo_m2.types.batch_job_step_list.deserialize_json(
            data["batchJobSteps"]
        )
    return out
