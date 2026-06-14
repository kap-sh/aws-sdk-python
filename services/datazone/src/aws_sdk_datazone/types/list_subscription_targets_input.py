"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionTargetsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.sort_key
    import aws_sdk_datazone.types.sort_order


class ListSubscriptionTargetsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain where you want to list subscription targets.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment where you want to list subscription targets.</p>"""
    sort_by: NotRequired["aws_sdk_datazone.types.sort_key.SortKey"]
    """<p>Specifies the way in which the results of this action are to be sorted.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order for the results of this action.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of subscription targets to return in a single call to <code>ListSubscriptionTargets</code>. When the number of subscription targets to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets. </p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscription targets is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription targets, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionTargetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionTargetsInput:
    out: ListSubscriptionTargetsInput = {}  # type: ignore[typeddict-item]
    return out
