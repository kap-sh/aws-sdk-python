"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_route53resolver.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the resource that you want to list tags for.</p>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of tags that you want to return in the response to a <code>ListTagsForResource</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 tags.</p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>For the first <code>ListTagsForResource</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> tags, you can submit another <code>ListTagsForResource</code> request to get the next group of tags for the resource. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
