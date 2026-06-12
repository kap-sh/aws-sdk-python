"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostCategoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_names_list
    import aws_sdk_cost_explorer.types.cost_category_values_list
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.page_size


class GetCostCategoriesResponse(TypedDict):
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>If the number of objects that are still available for retrieval exceeds the quota, Amazon Web Services returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    cost_category_names: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_names_list.CostCategoryNamesList"
    ]
    """<p>The names of the cost categories.</p>"""
    cost_category_values: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_values_list.CostCategoryValuesList"
    ]
    """<p>The cost category values.</p> <p>If the <code>CostCategoryName</code> key isn't specified in the request, the <code>CostCategoryValues</code> fields aren't returned. </p>"""
    return_size: "aws_sdk_cost_explorer.types.page_size.PageSize"
    """<p>The number of objects that are returned.</p>"""
    total_size: "aws_sdk_cost_explorer.types.page_size.PageSize"
    """<p>The total number of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostCategoriesResponse) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "cost_category_names" in value:
        import aws_sdk_cost_explorer.types.cost_category_names_list

        out["CostCategoryNames"] = (
            aws_sdk_cost_explorer.types.cost_category_names_list.serialize_aws_json_1_1(
                value["cost_category_names"]
            )
        )
    if "cost_category_values" in value:
        import aws_sdk_cost_explorer.types.cost_category_values_list

        out["CostCategoryValues"] = (
            aws_sdk_cost_explorer.types.cost_category_values_list.serialize_aws_json_1_1(
                value["cost_category_values"]
            )
        )
    out["ReturnSize"] = value["return_size"]
    out["TotalSize"] = value["total_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostCategoriesResponse:
    out: GetCostCategoriesResponse = {}  # type: ignore[typeddict-item]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "CostCategoryNames" in data:
        import aws_sdk_cost_explorer.types.cost_category_names_list

        out["cost_category_names"] = (
            aws_sdk_cost_explorer.types.cost_category_names_list.deserialize_aws_json_1_1(
                data["CostCategoryNames"]
            )
        )
    if "CostCategoryValues" in data:
        import aws_sdk_cost_explorer.types.cost_category_values_list

        out["cost_category_values"] = (
            aws_sdk_cost_explorer.types.cost_category_values_list.deserialize_aws_json_1_1(
                data["CostCategoryValues"]
            )
        )
    if "ReturnSize" in data:
        out["return_size"] = data["ReturnSize"]
    else:
        raise DeserializationError("GetCostCategoriesResponse.return_size required")
    if "TotalSize" in data:
        out["total_size"] = data["TotalSize"]
    else:
        raise DeserializationError("GetCostCategoriesResponse.total_size required")
    return out
