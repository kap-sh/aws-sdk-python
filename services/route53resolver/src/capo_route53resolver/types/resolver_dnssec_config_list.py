"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverDnssecConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_dnssec_config

ResolverDnssecConfigList: TypeAlias = list[
    "capo_route53resolver.types.resolver_dnssec_config.ResolverDnssecConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverDnssecConfigList) -> list:
    import capo_route53resolver.types.resolver_dnssec_config

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.resolver_dnssec_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverDnssecConfigList:
    import capo_route53resolver.types.resolver_dnssec_config

    out: ResolverDnssecConfigList = []
    for item in data:
        out.append(
            capo_route53resolver.types.resolver_dnssec_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
