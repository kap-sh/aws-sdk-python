"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkteamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.list_workteams_sort_by_options
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.workteam_name


class ListWorkteamsRequest(TypedDict, closed=True):
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_workteams_sort_by_options.ListWorkteamsSortByOptions"
    ]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.workteam_name.WorkteamName"]
    """<p>A string in the work team's name. This filter returns only work teams whose name contains the specified string.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListWorkteams</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of labeling jobs, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of work teams to return in each page of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkteamsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_workteams_sort_by_options

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_workteams_sort_by_options.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkteamsRequest:
    out: ListWorkteamsRequest = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_workteams_sort_by_options

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_workteams_sort_by_options.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
