"""Generated from Smithy shape ``com.amazonaws.glue#ListMLTransformsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token
    import capo_glue.types.tags_map
    import capo_glue.types.transform_filter_criteria
    import capo_glue.types.transform_sort_criteria


class ListMLTransformsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A continuation token, if this is a continuation request.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of a list to return.</p>"""
    filter: NotRequired[
        "capo_glue.types.transform_filter_criteria.TransformFilterCriteria"
    ]
    """<p>A <code>TransformFilterCriteria</code> used to filter the machine learning transforms.</p>"""
    sort: NotRequired["capo_glue.types.transform_sort_criteria.TransformSortCriteria"]
    """<p>A <code>TransformSortCriteria</code> used to sort the machine learning transforms.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>Specifies to return only these tagged resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMLTransformsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import capo_glue.types.transform_filter_criteria

        out["Filter"] = (
            capo_glue.types.transform_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "sort" in value:
        import capo_glue.types.transform_sort_criteria

        out["Sort"] = capo_glue.types.transform_sort_criteria.serialize_aws_json_1_1(
            value["sort"]
        )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMLTransformsRequest:
    out: ListMLTransformsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filter" in data:
        import capo_glue.types.transform_filter_criteria

        out["filter"] = (
            capo_glue.types.transform_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "Sort" in data:
        import capo_glue.types.transform_sort_criteria

        out["sort"] = capo_glue.types.transform_sort_criteria.deserialize_aws_json_1_1(
            data["Sort"]
        )
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
