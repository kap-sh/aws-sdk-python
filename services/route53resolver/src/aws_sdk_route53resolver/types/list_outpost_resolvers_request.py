"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListOutpostResolversRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.outpost_arn


class ListOutpostResolversRequest(TypedDict):
    outpost_arn: NotRequired["aws_sdk_route53resolver.types.outpost_arn.OutpostArn"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of Resolvers on the Outpost that you want to return in the response to a <code>ListOutpostResolver</code> request. If you don't specify a value for <code>MaxResults</code>, the request returns up to 100 Resolvers.</p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>For the first <code>ListOutpostResolver</code> request, omit this value.</p> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOutpostResolversRequest) -> dict:
    out: dict = {}
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOutpostResolversRequest:
    out: ListOutpostResolversRequest = {}  # type: ignore[typeddict-item]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
