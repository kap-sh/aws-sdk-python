"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionGrantsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.group_profile_id
    import aws_sdk_datazone.types.iam_principal_arn
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.sort_key
    import aws_sdk_datazone.types.sort_order
    import aws_sdk_datazone.types.subscription_id
    import aws_sdk_datazone.types.subscription_target_id
    import aws_sdk_datazone.types.user_profile_id


class ListSubscriptionGrantsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The identifier of the Amazon DataZone environment.</p>"""
    subscription_target_id: NotRequired[
        "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    ]
    """<p>The identifier of the subscription target.</p>"""
    subscribed_listing_id: NotRequired["aws_sdk_datazone.types.listing_id.ListingId"]
    """<p>The identifier of the subscribed listing.</p>"""
    subscription_id: NotRequired[
        "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    ]
    """<p>The identifier of the subscription.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the owning project of the subscription grants.</p>"""
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
    sort_by: NotRequired["aws_sdk_datazone.types.sort_key.SortKey"]
    """<p>Specifies the way of sorting the results of this action.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order of this action.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of subscription grants to return in a single call to <code>ListSubscriptionGrants</code>. When the number of subscription grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscription grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionGrantsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionGrantsInput:
    out: ListSubscriptionGrantsInput = {}  # type: ignore[typeddict-item]
    return out
