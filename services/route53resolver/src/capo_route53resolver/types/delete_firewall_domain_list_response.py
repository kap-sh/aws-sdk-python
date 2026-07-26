"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallDomainListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_domain_list


class DeleteFirewallDomainListResponse(TypedDict, closed=True):
    firewall_domain_list: NotRequired[
        "capo_route53resolver.types.firewall_domain_list.FirewallDomainList"
    ]
    """<p>The domain list that you just deleted. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallDomainListResponse) -> dict:
    out: dict = {}
    if "firewall_domain_list" in value:
        import capo_route53resolver.types.firewall_domain_list

        out["FirewallDomainList"] = (
            capo_route53resolver.types.firewall_domain_list.serialize_aws_json_1_1(
                value["firewall_domain_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallDomainListResponse:
    out: DeleteFirewallDomainListResponse = {}  # type: ignore[typeddict-item]
    if "FirewallDomainList" in data:
        import capo_route53resolver.types.firewall_domain_list

        out["firewall_domain_list"] = (
            capo_route53resolver.types.firewall_domain_list.deserialize_aws_json_1_1(
                data["FirewallDomainList"]
            )
        )
    return out
