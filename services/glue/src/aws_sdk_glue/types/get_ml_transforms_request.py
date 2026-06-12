"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTransformsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.transform_filter_criteria
    import aws_sdk_glue.types.transform_sort_criteria


class GetMLTransformsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    filter: NotRequired[
        "aws_sdk_glue.types.transform_filter_criteria.TransformFilterCriteria"
    ]
    """<p>The filter transformation criteria.</p>"""
    sort: NotRequired[
        "aws_sdk_glue.types.transform_sort_criteria.TransformSortCriteria"
    ]
    """<p>The sorting criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTransformsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_glue.types.transform_filter_criteria

        out["Filter"] = (
            aws_sdk_glue.types.transform_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "sort" in value:
        import aws_sdk_glue.types.transform_sort_criteria

        out["Sort"] = aws_sdk_glue.types.transform_sort_criteria.serialize_aws_json_1_1(
            value["sort"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTransformsRequest:
    out: GetMLTransformsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filter" in data:
        import aws_sdk_glue.types.transform_filter_criteria

        out["filter"] = (
            aws_sdk_glue.types.transform_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "Sort" in data:
        import aws_sdk_glue.types.transform_sort_criteria

        out["sort"] = (
            aws_sdk_glue.types.transform_sort_criteria.deserialize_aws_json_1_1(
                data["Sort"]
            )
        )
    return out
