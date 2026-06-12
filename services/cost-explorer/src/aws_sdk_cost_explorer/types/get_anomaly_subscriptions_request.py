"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomalySubscriptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.page_size
    import aws_sdk_cost_explorer.types.values


class GetAnomalySubscriptionsRequest(TypedDict):
    subscription_arn_list: NotRequired["aws_sdk_cost_explorer.types.values.Values"]
    """<p>A list of cost anomaly subscription ARNs. </p>"""
    monitor_arn: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>Cost anomaly monitor ARNs. </p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired["aws_sdk_cost_explorer.types.page_size.PageSize"]
    """<p>The number of entries a paginated response contains. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomalySubscriptionsRequest) -> dict:
    out: dict = {}
    if "subscription_arn_list" in value:
        import aws_sdk_cost_explorer.types.values

        out["SubscriptionArnList"] = (
            aws_sdk_cost_explorer.types.values.serialize_aws_json_1_1(
                value["subscription_arn_list"]
            )
        )
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomalySubscriptionsRequest:
    out: GetAnomalySubscriptionsRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionArnList" in data:
        import aws_sdk_cost_explorer.types.values

        out["subscription_arn_list"] = (
            aws_sdk_cost_explorer.types.values.deserialize_aws_json_1_1(
                data["SubscriptionArnList"]
            )
        )
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
