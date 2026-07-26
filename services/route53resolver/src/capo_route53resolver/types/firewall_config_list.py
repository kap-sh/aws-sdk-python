"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_config

FirewallConfigList: TypeAlias = list[
    "capo_route53resolver.types.firewall_config.FirewallConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallConfigList) -> list:
    import capo_route53resolver.types.firewall_config

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallConfigList:
    import capo_route53resolver.types.firewall_config

    out: FirewallConfigList = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_config.deserialize_aws_json_1_1(item)
        )
    return out
