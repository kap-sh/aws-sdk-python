"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkforcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.list_workforces_sort_by_options
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.workforce_name


class ListWorkforcesRequest(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_sagemaker.types.list_workforces_sort_by_options.ListWorkforcesSortByOptions"
    ]
    """<p>Sort workforces using the workforce name or creation date.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>Sort workforces in ascending or descending order.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.workforce_name.WorkforceName"]
    """<p>A filter you can use to search for workforces using part of the workforce name.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of workforces returned in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkforcesRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_sagemaker.types.list_workforces_sort_by_options

        out["SortBy"] = (
            capo_sagemaker.types.list_workforces_sort_by_options.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkforcesRequest:
    out: ListWorkforcesRequest = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import capo_sagemaker.types.list_workforces_sort_by_options

        out["sort_by"] = (
            capo_sagemaker.types.list_workforces_sort_by_options.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
