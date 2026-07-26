"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer
    import capo_macie2.types.__string
    import capo_macie2.types.search_resources_bucket_criteria
    import capo_macie2.types.search_resources_sort_criteria


class SearchResourcesRequest(TypedDict, closed=True):
    bucket_criteria: NotRequired[
        "capo_macie2.types.search_resources_bucket_criteria.SearchResourcesBucketCriteria"
    ]
    """<p>The filter conditions that determine which S3 buckets to include or exclude from the query results.</p>"""
    max_results: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response. The default value is 50.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_criteria: NotRequired[
        "capo_macie2.types.search_resources_sort_criteria.SearchResourcesSortCriteria"
    ]
    """<p>The criteria to use to sort the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesRequest) -> dict:
    out: dict = {}
    if "bucket_criteria" in value:
        import capo_macie2.types.search_resources_bucket_criteria

        out["bucketCriteria"] = (
            capo_macie2.types.search_resources_bucket_criteria.serialize_json(
                value["bucket_criteria"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_criteria" in value:
        import capo_macie2.types.search_resources_sort_criteria

        out["sortCriteria"] = (
            capo_macie2.types.search_resources_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesRequest:
    out: SearchResourcesRequest = {}  # type: ignore[typeddict-item]
    if "bucketCriteria" in data:
        import capo_macie2.types.search_resources_bucket_criteria

        out["bucket_criteria"] = (
            capo_macie2.types.search_resources_bucket_criteria.deserialize_json(
                data["bucketCriteria"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortCriteria" in data:
        import capo_macie2.types.search_resources_sort_criteria

        out["sort_criteria"] = (
            capo_macie2.types.search_resources_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
