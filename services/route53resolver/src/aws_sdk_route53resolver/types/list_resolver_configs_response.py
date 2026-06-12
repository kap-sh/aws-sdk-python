"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.resolver_config_list


class ListResolverConfigsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If a response includes the last of the Resolver configurations that are associated with the current Amazon Web Services account, <code>NextToken</code> doesn't appear in the response.</p> <p>If a response doesn't include the last of the configurations, you can get more configurations by submitting another <code>ListResolverConfigs</code> request. Get the value of <code>NextToken</code> that Amazon Route 53 returned in the previous response and include it in <code>NextToken</code> in the next request.</p>"""
    resolver_configs: NotRequired[
        "aws_sdk_route53resolver.types.resolver_config_list.ResolverConfigList"
    ]
    """<p>An array that contains one <code>ResolverConfigs</code> element for each Resolver configuration that is associated with the current Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resolver_configs" in value:
        import aws_sdk_route53resolver.types.resolver_config_list

        out["ResolverConfigs"] = (
            aws_sdk_route53resolver.types.resolver_config_list.serialize_aws_json_1_1(
                value["resolver_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverConfigsResponse:
    out: ListResolverConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResolverConfigs" in data:
        import aws_sdk_route53resolver.types.resolver_config_list

        out["resolver_configs"] = (
            aws_sdk_route53resolver.types.resolver_config_list.deserialize_aws_json_1_1(
                data["ResolverConfigs"]
            )
        )
    return out
