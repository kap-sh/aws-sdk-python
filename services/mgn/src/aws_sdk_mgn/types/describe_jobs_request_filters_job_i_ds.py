"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobsRequestFiltersJobIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job_id

DescribeJobsRequestFiltersJobIDs: TypeAlias = list["aws_sdk_mgn.types.job_id.JobID"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequestFiltersJobIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeJobsRequestFiltersJobIDs:
    return list(data)
