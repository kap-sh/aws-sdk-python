"""Generated from Smithy shape ``com.amazonaws.route53profiles#ListProfileResourceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.max_results
    import aws_sdk_route53profiles.types.next_token
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.string


class ListProfileResourceAssociationsRequest(TypedDict):
    profile_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the Profile. </p>"""
    resource_type: NotRequired["aws_sdk_route53profiles.types.string.String"]
    """<p> ID of a resource if you want information on only one type. </p>"""
    max_results: NotRequired["aws_sdk_route53profiles.types.max_results.MaxResults"]
    """<p> The maximum number of objects that you want to return for this request. If more objects are available, in the response, a <code>NextToken</code> value, which you can use in a subsequent call to get the next batch of objects, is provided.</p> <p> If you don't specify a value for <code>MaxResults</code>, up to 100 objects are returned. </p>"""
    next_token: NotRequired["aws_sdk_route53profiles.types.next_token.NextToken"]
    """<p> For the first call to this list request, omit this value. </p> <p>When you request a list of objects, at most the number of objects specified by <code>MaxResults</code> is returned. If more objects are available for retrieval, a <code>NextToken</code> value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileResourceAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileResourceAssociationsRequest:
    out: ListProfileResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
