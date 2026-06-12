"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSharedReportGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.shared_resource_sort_by_type
    import aws_sdk_codebuild.types.sort_order_type
    import aws_sdk_codebuild.types.string


class ListSharedReportGroupsInput(TypedDict):
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which to list shared report groups. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul>"""
    sort_by: NotRequired[
        "aws_sdk_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
    ]
    """<p> The criterion to be used to list report groups shared with the current Amazon Web Services account or user. Valid values include: </p> <ul> <li> <p> <code>ARN</code>: List based on the ARN. </p> </li> <li> <p> <code>MODIFIED_TIME</code>: List based on when information about the shared report group was last changed. </p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated shared report groups per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>ReportGroup</code> objects. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSharedReportGroupsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_codebuild.types.shared_resource_sort_by_type

        out["sortBy"] = (
            aws_sdk_codebuild.types.shared_resource_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSharedReportGroupsInput:
    out: ListSharedReportGroupsInput = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "sortBy" in data:
        import aws_sdk_codebuild.types.shared_resource_sort_by_type

        out["sort_by"] = (
            aws_sdk_codebuild.types.shared_resource_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
