"""Generated from Smithy shape ``com.amazonaws.drs#DescribeJobsRequestFiltersJobIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.job_id

DescribeJobsRequestFiltersJobIDs: TypeAlias = list["capo_drs.types.job_id.JobID"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequestFiltersJobIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeJobsRequestFiltersJobIDs:
    return list(data)
