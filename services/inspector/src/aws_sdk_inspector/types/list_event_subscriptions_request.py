"""Generated from Smithy shape ``com.amazonaws.inspector#ListEventSubscriptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.list_event_subscriptions_max_results
    import aws_sdk_inspector.types.pagination_token


class ListEventSubscriptionsRequest(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The ARN of the assessment template for which you want to list the existing event subscriptions.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListEventSubscriptions</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>"""
    max_results: NotRequired[
        "aws_sdk_inspector.types.list_event_subscriptions_max_results.ListEventSubscriptionsMaxResults"
    ]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSubscriptionsRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSubscriptionsRequest:
    out: ListEventSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
