"""Generated from Smithy shape ``com.amazonaws.databrew#StopJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_name
    import capo_databrew.types.job_run_id


class StopJobRunRequest(TypedDict, closed=True):
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job to be stopped.</p>"""
    run_id: "capo_databrew.types.job_run_id.JobRunId"
    """<p>The ID of the job run to be stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopJobRunRequest:
    out: StopJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
