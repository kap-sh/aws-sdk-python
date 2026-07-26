"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.job_detail_list


class DescribeJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_batch.types.job_detail_list.JobDetailList"]
    """<p>The list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_batch.types.job_detail_list

        out["jobs"] = capo_batch.types.job_detail_list.serialize_json(value["jobs"])
    return out


def deserialize_json(data: dict) -> DescribeJobsResponse:
    out: DescribeJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_batch.types.job_detail_list

        out["jobs"] = capo_batch.types.job_detail_list.deserialize_json(data["jobs"])
    return out
