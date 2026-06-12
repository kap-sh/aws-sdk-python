"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostCategoriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.billing_view_arn
    import aws_sdk_cost_explorer.types.cost_category_name
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.max_results
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.search_string
    import aws_sdk_cost_explorer.types.sort_definitions


class GetCostCategoriesRequest(TypedDict):
    search_string: NotRequired["aws_sdk_cost_explorer.types.search_string.SearchString"]
    """<p>The value that you want to search the filter values for.</p> <p>If you don't specify a <code>CostCategoryName</code>, <code>SearchString</code> is used to filter cost category names that match the <code>SearchString</code> pattern. If you specify a <code>CostCategoryName</code>, <code>SearchString</code> is used to filter cost category values that match the <code>SearchString</code> pattern.</p>"""
    time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    cost_category_name: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"
    ]
    filter: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    sort_by: NotRequired["aws_sdk_cost_explorer.types.sort_definitions.SortDefinitions"]
    """<p>The value that you sort the data by.</p> <p>The key represents the cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported key values for the <code>SortOrder</code> value are <code>ASCENDING</code> and <code>DESCENDING</code>.</p> <p>When you use the <code>SortBy</code> value, the <code>NextPageToken</code> and <code>SearchString</code> key values aren't supported.</p>"""
    billing_view_arn: NotRequired[
        "aws_sdk_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    max_results: NotRequired["aws_sdk_cost_explorer.types.max_results.MaxResults"]
    """<p>This field is only used when the <code>SortBy</code> value is provided in the request.</p> <p>The maximum number of objects that are returned for this request. If <code>MaxResults</code> isn't specified with the <code>SortBy</code> value, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetCostCategories</code>, MaxResults has an upper quota of 1000.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>If the number of objects that are still available for retrieval exceeds the quota, Amazon Web Services returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the NextPageToken from the previous call in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostCategoriesRequest) -> dict:
    out: dict = {}
    if "search_string" in value:
        out["SearchString"] = value["search_string"]
    import aws_sdk_cost_explorer.types.date_interval

    out["TimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["time_period"]
        )
    )
    if "cost_category_name" in value:
        out["CostCategoryName"] = value["cost_category_name"]
    if "filter" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Filter"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "sort_by" in value:
        import aws_sdk_cost_explorer.types.sort_definitions

        out["SortBy"] = (
            aws_sdk_cost_explorer.types.sort_definitions.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostCategoriesRequest:
    out: GetCostCategoriesRequest = {}  # type: ignore[typeddict-item]
    if "SearchString" in data:
        out["search_string"] = data["SearchString"]
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError("GetCostCategoriesRequest.time_period required")
    if "CostCategoryName" in data:
        out["cost_category_name"] = data["CostCategoryName"]
    if "Filter" in data:
        import aws_sdk_cost_explorer.types.expression

        out["filter"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if "SortBy" in data:
        import aws_sdk_cost_explorer.types.sort_definitions

        out["sort_by"] = (
            aws_sdk_cost_explorer.types.sort_definitions.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "BillingViewArn" in data:
        out["billing_view_arn"] = data["BillingViewArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
