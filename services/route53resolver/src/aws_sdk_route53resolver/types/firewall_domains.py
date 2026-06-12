"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_domain_name

FirewallDomains: TypeAlias = list[
    "aws_sdk_route53resolver.types.firewall_domain_name.FirewallDomainName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomains) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FirewallDomains:
    return list(data)
