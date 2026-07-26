"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_configuration_metadata

ProxyConfigurations: TypeAlias = list[
    "capo_network_firewall.types.proxy_configuration_metadata.ProxyConfigurationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyConfigurations) -> list:
    import capo_network_firewall.types.proxy_configuration_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.proxy_configuration_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyConfigurations:
    import capo_network_firewall.types.proxy_configuration_metadata

    out: ProxyConfigurations = []
    for item in data:
        out.append(
            capo_network_firewall.types.proxy_configuration_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
