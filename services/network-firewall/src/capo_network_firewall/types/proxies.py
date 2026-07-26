"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Proxies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_metadata

Proxies: TypeAlias = list["capo_network_firewall.types.proxy_metadata.ProxyMetadata"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Proxies) -> list:
    import capo_network_firewall.types.proxy_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.proxy_metadata.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Proxies:
    import capo_network_firewall.types.proxy_metadata

    out: Proxies = []
    for item in data:
        out.append(
            capo_network_firewall.types.proxy_metadata.deserialize_aws_json_1_0(item)
        )
    return out
