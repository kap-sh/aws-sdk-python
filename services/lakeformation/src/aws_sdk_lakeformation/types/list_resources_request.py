"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.filter_condition_list
    import aws_sdk_lakeformation.types.page_size
    import aws_sdk_lakeformation.types.token


class ListResourcesRequest(TypedDict):
    filter_condition_list: NotRequired[
        "aws_sdk_lakeformation.types.filter_condition_list.FilterConditionList"
    ]
    """<p>Any applicable row-level and/or column-level filtering conditions for the resources.</p>"""
    max_results: NotRequired["aws_sdk_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of resource results.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve these resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesRequest) -> dict:
    out: dict = {}
    if "filter_condition_list" in value:
        import aws_sdk_lakeformation.types.filter_condition_list

        out["FilterConditionList"] = (
            aws_sdk_lakeformation.types.filter_condition_list.serialize_json(
                value["filter_condition_list"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesRequest:
    out: ListResourcesRequest = {}  # type: ignore[typeddict-item]
    if "FilterConditionList" in data:
        import aws_sdk_lakeformation.types.filter_condition_list

        out["filter_condition_list"] = (
            aws_sdk_lakeformation.types.filter_condition_list.deserialize_json(
                data["FilterConditionList"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
