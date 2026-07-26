"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListOutpostResolversResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.outpost_resolver_list


class ListOutpostResolversResponse(TypedDict, closed=True):
    outpost_resolvers: NotRequired[
        "capo_route53resolver.types.outpost_resolver_list.OutpostResolverList"
    ]
    """<p>The Resolvers on Outposts that were created by using the current Amazon Web Services account, and that match the specified filters, if any.</p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> Resolvers match the specified criteria, you can submit another <code>ListOutpostResolver</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOutpostResolversResponse) -> dict:
    out: dict = {}
    if "outpost_resolvers" in value:
        import capo_route53resolver.types.outpost_resolver_list

        out["OutpostResolvers"] = (
            capo_route53resolver.types.outpost_resolver_list.serialize_aws_json_1_1(
                value["outpost_resolvers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOutpostResolversResponse:
    out: ListOutpostResolversResponse = {}  # type: ignore[typeddict-item]
    if "OutpostResolvers" in data:
        import capo_route53resolver.types.outpost_resolver_list

        out["outpost_resolvers"] = (
            capo_route53resolver.types.outpost_resolver_list.deserialize_aws_json_1_1(
                data["OutpostResolvers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
