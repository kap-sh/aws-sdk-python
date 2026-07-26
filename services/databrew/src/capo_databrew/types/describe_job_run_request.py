"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_name
    import capo_databrew.types.job_run_id


class DescribeJobRunRequest(TypedDict, closed=True):
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job being processed during this run.</p>"""
    run_id: "capo_databrew.types.job_run_id.JobRunId"
    """<p>The unique identifier of the job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobRunRequest:
    out: DescribeJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
