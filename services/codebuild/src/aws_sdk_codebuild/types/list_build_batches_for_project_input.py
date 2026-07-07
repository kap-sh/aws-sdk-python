"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildBatchesForProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch_filter
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.sort_order_type
    import aws_sdk_codebuild.types.string


class ListBuildBatchesForProjectInput(TypedDict, closed=True):
    project_name: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of the project.</p>"""
    filter: NotRequired["aws_sdk_codebuild.types.build_batch_filter.BuildBatchFilter"]
    """<p>A <code>BuildBatchFilter</code> object that specifies the filters for the search.</p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>Specifies the sort order of the returned items. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the batch build identifiers in ascending order by identifier.</p> </li> <li> <p> <code>DESCENDING</code>: List the batch build identifiers in descending order by identifier.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous call to <code>ListBuildBatchesForProject</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildBatchesForProjectInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "filter" in value:
        import aws_sdk_codebuild.types.build_batch_filter

        out["filter"] = (
            aws_sdk_codebuild.types.build_batch_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildBatchesForProjectInput:
    out: ListBuildBatchesForProjectInput = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "filter" in data:
        import aws_sdk_codebuild.types.build_batch_filter

        out["filter"] = (
            aws_sdk_codebuild.types.build_batch_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
