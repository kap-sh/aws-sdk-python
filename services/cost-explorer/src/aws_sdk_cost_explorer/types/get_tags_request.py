"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.billing_view_arn
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.max_results
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.search_string
    import aws_sdk_cost_explorer.types.sort_definitions
    import aws_sdk_cost_explorer.types.tag_key


class GetTagsRequest(TypedDict):
    search_string: NotRequired["aws_sdk_cost_explorer.types.search_string.SearchString"]
    """<p>The value that you want to search for.</p>"""
    time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    """<p>The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>"""
    tag_key: NotRequired["aws_sdk_cost_explorer.types.tag_key.TagKey"]
    """<p>The key of the tag that you want to return values for.</p>"""
    filter: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    sort_by: NotRequired["aws_sdk_cost_explorer.types.sort_definitions.SortDefinitions"]
    """<p>The value that you want to sort the data by.</p> <p>The key represents cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p> <p>When you use <code>SortBy</code>, <code>NextPageToken</code> and <code>SearchString</code> aren't supported.</p>"""
    billing_view_arn: NotRequired[
        "aws_sdk_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    max_results: NotRequired["aws_sdk_cost_explorer.types.max_results.MaxResults"]
    """<p>This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetTags</code>, MaxResults has an upper quota of 1000.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsRequest) -> dict:
    out: dict = {}
    if "search_string" in value:
        out["SearchString"] = value["search_string"]
    import aws_sdk_cost_explorer.types.date_interval

    out["TimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["time_period"]
        )
    )
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
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


def deserialize_aws_json_1_1(data: dict) -> GetTagsRequest:
    out: GetTagsRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("GetTagsRequest.time_period required")
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
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
