"""Generated from Smithy shape ``com.amazonaws.glacier#ListJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.job_list
    import capo_glacier.types.string


class ListJobsOutput(TypedDict, closed=True):
    job_list: NotRequired["capo_glacier.types.job_list.JobList"]
    """<p>A list of job objects. Each job object contains metadata describing the job.</p>"""
    marker: NotRequired["capo_glacier.types.string.string"]
    """<p> An opaque string used for pagination that specifies the job at which the listing of jobs should begin. You get the <code>marker</code> value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of the results started in a previous List Jobs request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsOutput) -> dict:
    out: dict = {}
    if "job_list" in value:
        import capo_glacier.types.job_list

        out["JobList"] = capo_glacier.types.job_list.serialize_json(value["job_list"])
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> ListJobsOutput:
    out: ListJobsOutput = {}  # type: ignore[typeddict-item]
    if "JobList" in data:
        import capo_glacier.types.job_list

        out["job_list"] = capo_glacier.types.job_list.deserialize_json(data["JobList"])
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
