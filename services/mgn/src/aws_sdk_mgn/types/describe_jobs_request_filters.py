"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobsRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds
    import aws_sdk_mgn.types.iso8601_datetime_string


class DescribeJobsRequestFilters(TypedDict):
    job_i_ds: NotRequired[
        "aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds.DescribeJobsRequestFiltersJobIDs"
    ]
    """<p>Request to describe Job log filters by job ID.</p>"""
    from_date: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to describe Job log filters by date.</p>"""
    to_date: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to describe job log items by last date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequestFilters) -> dict:
    out: dict = {}
    if "job_i_ds" in value:
        import aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds

        out["jobIDs"] = (
            aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds.serialize_json(
                value["job_i_ds"]
            )
        )
    if "from_date" in value:
        out["fromDate"] = value["from_date"]
    if "to_date" in value:
        out["toDate"] = value["to_date"]
    return out


def deserialize_json(data: dict) -> DescribeJobsRequestFilters:
    out: DescribeJobsRequestFilters = {}  # type: ignore[typeddict-item]
    if "jobIDs" in data:
        import aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds

        out["job_i_ds"] = (
            aws_sdk_mgn.types.describe_jobs_request_filters_job_i_ds.deserialize_json(
                data["jobIDs"]
            )
        )
    if "fromDate" in data:
        out["from_date"] = data["fromDate"]
    if "toDate" in data:
        out["to_date"] = data["toDate"]
    return out
