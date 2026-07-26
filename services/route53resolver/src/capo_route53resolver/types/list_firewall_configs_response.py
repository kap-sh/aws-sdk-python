"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_config_list
    import capo_route53resolver.types.next_token


class ListFirewallConfigsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    firewall_configs: NotRequired[
        "capo_route53resolver.types.firewall_config_list.FirewallConfigList"
    ]
    """<p>The configurations for the firewall behavior provided by DNS Firewall for VPCs from Amazon Virtual Private Cloud (Amazon VPC). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_configs" in value:
        import capo_route53resolver.types.firewall_config_list

        out["FirewallConfigs"] = (
            capo_route53resolver.types.firewall_config_list.serialize_aws_json_1_1(
                value["firewall_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallConfigsResponse:
    out: ListFirewallConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FirewallConfigs" in data:
        import capo_route53resolver.types.firewall_config_list

        out["firewall_configs"] = (
            capo_route53resolver.types.firewall_config_list.deserialize_aws_json_1_1(
                data["FirewallConfigs"]
            )
        )
    return out
