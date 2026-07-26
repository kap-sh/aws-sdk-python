"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_profile_id
    import capo_datazone.types.iam_principal_arn
    import capo_datazone.types.listing_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_id
    import capo_datazone.types.sort_key
    import capo_datazone.types.sort_order
    import capo_datazone.types.subscription_request_status
    import capo_datazone.types.user_profile_id


class ListSubscriptionRequestsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    status: NotRequired[
        "capo_datazone.types.subscription_request_status.SubscriptionRequestStatus"
    ]
    """<p>Specifies the status of the subscription requests.</p> <note> <p>This is not a required parameter, but if not specified, by default, Amazon DataZone returns only <code>PENDING</code> subscription requests. </p> </note>"""
    subscribed_listing_id: NotRequired["capo_datazone.types.listing_id.ListingId"]
    """<p>The identifier of the subscribed listing.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project for the subscription requests.</p>"""
    owning_iam_principal_arn: NotRequired[
        "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
    ]
    """<p>The ARN of the owning IAM principal.</p>"""
    approver_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the subscription request approver's project.</p>"""
    owning_user_id: NotRequired["capo_datazone.types.user_profile_id.UserProfileId"]
    """<p>The ID of the owning user.</p>"""
    owning_group_id: NotRequired["capo_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The ID of the owning group.</p>"""
    sort_by: NotRequired["capo_datazone.types.sort_key.SortKey"]
    """<p>Specifies the way to sort the results of this action.</p>"""
    sort_order: NotRequired["capo_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order for the results of this action.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of subscription requests to return in a single call to <code>ListSubscriptionRequests</code>. When the number of subscription requests to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscription requests is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription requests, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionRequestsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionRequestsInput:
    out: ListSubscriptionRequestsInput = {}  # type: ignore[typeddict-item]
    return out
