"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainListMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_domain_list_metadata

FirewallDomainListMetadataList: TypeAlias = list[
    "capo_route53resolver.types.firewall_domain_list_metadata.FirewallDomainListMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainListMetadataList) -> list:
    import capo_route53resolver.types.firewall_domain_list_metadata

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_domain_list_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallDomainListMetadataList:
    import capo_route53resolver.types.firewall_domain_list_metadata

    out: FirewallDomainListMetadataList = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_domain_list_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
