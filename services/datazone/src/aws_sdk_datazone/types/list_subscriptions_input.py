"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.group_profile_id
    import aws_sdk_datazone.types.iam_principal_arn
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.sort_key
    import aws_sdk_datazone.types.sort_order
    import aws_sdk_datazone.types.subscription_request_id
    import aws_sdk_datazone.types.subscription_status
    import aws_sdk_datazone.types.user_profile_id


class ListSubscriptionsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    subscription_request_identifier: NotRequired[
        "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    ]
    """<p>The identifier of the subscription request for the subscriptions that you want to list.</p>"""
    status: NotRequired["aws_sdk_datazone.types.subscription_status.SubscriptionStatus"]
    """<p>The status of the subscriptions that you want to list.</p> <note> <p>This is not a required parameter, but if not provided, by default, Amazon DataZone returns only <code>APPROVED</code> subscriptions. </p> </note>"""
    subscribed_listing_id: NotRequired["aws_sdk_datazone.types.listing_id.ListingId"]
    """<p>The identifier of the subscribed listing for the subscriptions that you want to list.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the owning project.</p>"""
    owning_iam_principal_arn: NotRequired[
        "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
    ]
    """<p>The ARN of the owning IAM principal.</p>"""
    owning_user_id: NotRequired["aws_sdk_datazone.types.user_profile_id.UserProfileId"]
    """<p>The ID of the owning user.</p>"""
    owning_group_id: NotRequired[
        "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
    ]
    """<p>The ID of the owning group.</p>"""
    approver_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project for the subscription's approver.</p>"""
    sort_by: NotRequired["aws_sdk_datazone.types.sort_key.SortKey"]
    """<p>Specifies the way in which the results of this action are to be sorted.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order for the results of this action.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of subscriptions to return in a single call to <code>ListSubscriptions</code>. When the number of subscriptions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptions</code> to list the next set of Subscriptions. </p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscriptions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscriptions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptions</code> to list the next set of subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionsInput:
    out: ListSubscriptionsInput = {}  # type: ignore[typeddict-item]
    return out
