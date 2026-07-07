"""Generated from Smithy shape ``com.amazonaws.macie2#ListClassificationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.list_jobs_filter_criteria
    import aws_sdk_macie2.types.list_jobs_sort_criteria


class ListClassificationJobsRequest(TypedDict, closed=True):
    filter_criteria: NotRequired[
        "aws_sdk_macie2.types.list_jobs_filter_criteria.ListJobsFilterCriteria"
    ]
    """<p>The criteria to use to filter the results.</p>"""
    max_results: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_criteria: NotRequired[
        "aws_sdk_macie2.types.list_jobs_sort_criteria.ListJobsSortCriteria"
    ]
    """<p>The criteria to use to sort the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClassificationJobsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_macie2.types.list_jobs_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_macie2.types.list_jobs_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_criteria" in value:
        import aws_sdk_macie2.types.list_jobs_sort_criteria

        out["sortCriteria"] = (
            aws_sdk_macie2.types.list_jobs_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListClassificationJobsRequest:
    out: ListClassificationJobsRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_macie2.types.list_jobs_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_macie2.types.list_jobs_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortCriteria" in data:
        import aws_sdk_macie2.types.list_jobs_sort_criteria

        out["sort_criteria"] = (
            aws_sdk_macie2.types.list_jobs_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
