"""Generated from Smithy shape ``com.amazonaws.drs#DescribeJobsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.describe_jobs_request_filters_job_i_ds
    import capo_drs.types.iso8601_datetime_string


class DescribeJobsRequestFilters(TypedDict, closed=True):
    job_i_ds: NotRequired[
        "capo_drs.types.describe_jobs_request_filters_job_i_ds.DescribeJobsRequestFiltersJobIDs"
    ]
    """<p>An array of Job IDs that should be returned. An empty array means all jobs.</p>"""
    from_date: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The start date in a date range query.</p>"""
    to_date: NotRequired["capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The end date in a date range query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequestFilters) -> dict:
    out: dict = {}
    if "job_i_ds" in value:
        import capo_drs.types.describe_jobs_request_filters_job_i_ds

        out["jobIDs"] = (
            capo_drs.types.describe_jobs_request_filters_job_i_ds.serialize_json(
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
        import capo_drs.types.describe_jobs_request_filters_job_i_ds

        out["job_i_ds"] = (
            capo_drs.types.describe_jobs_request_filters_job_i_ds.deserialize_json(
                data["jobIDs"]
            )
        )
    if "fromDate" in data:
        out["from_date"] = data["fromDate"]
    if "toDate" in data:
        out["to_date"] = data["toDate"]
    return out
