"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.bucket_criteria
    import aws_sdk_macie2.types.bucket_sort_criteria


class DescribeBucketsRequest(TypedDict, closed=True):
    criteria: NotRequired["aws_sdk_macie2.types.bucket_criteria.BucketCriteria"]
    """<p>The criteria to use to filter the query results.</p>"""
    max_results: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response. The default value is 50.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_criteria: NotRequired[
        "aws_sdk_macie2.types.bucket_sort_criteria.BucketSortCriteria"
    ]
    """<p>The criteria to use to sort the query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBucketsRequest) -> dict:
    out: dict = {}
    if "criteria" in value:
        import aws_sdk_macie2.types.bucket_criteria

        out["criteria"] = aws_sdk_macie2.types.bucket_criteria.serialize_json(
            value["criteria"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_criteria" in value:
        import aws_sdk_macie2.types.bucket_sort_criteria

        out["sortCriteria"] = aws_sdk_macie2.types.bucket_sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> DescribeBucketsRequest:
    out: DescribeBucketsRequest = {}  # type: ignore[typeddict-item]
    if "criteria" in data:
        import aws_sdk_macie2.types.bucket_criteria

        out["criteria"] = aws_sdk_macie2.types.bucket_criteria.deserialize_json(
            data["criteria"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortCriteria" in data:
        import aws_sdk_macie2.types.bucket_sort_criteria

        out["sort_criteria"] = (
            aws_sdk_macie2.types.bucket_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
