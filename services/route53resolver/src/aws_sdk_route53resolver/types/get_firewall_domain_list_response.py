"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallDomainListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_domain_list


class GetFirewallDomainListResponse(TypedDict, closed=True):
    firewall_domain_list: NotRequired[
        "aws_sdk_route53resolver.types.firewall_domain_list.FirewallDomainList"
    ]
    """<p>The domain list that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallDomainListResponse) -> dict:
    out: dict = {}
    if "firewall_domain_list" in value:
        import aws_sdk_route53resolver.types.firewall_domain_list

        out["FirewallDomainList"] = (
            aws_sdk_route53resolver.types.firewall_domain_list.serialize_aws_json_1_1(
                value["firewall_domain_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallDomainListResponse:
    out: GetFirewallDomainListResponse = {}  # type: ignore[typeddict-item]
    if "FirewallDomainList" in data:
        import aws_sdk_route53resolver.types.firewall_domain_list

        out["firewall_domain_list"] = (
            aws_sdk_route53resolver.types.firewall_domain_list.deserialize_aws_json_1_1(
                data["FirewallDomainList"]
            )
        )
    return out
