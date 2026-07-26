"""Generated from Smithy shape ``com.amazonaws.directoryservice#DnsIpv6Addrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ipv6_addr

DnsIpv6Addrs: TypeAlias = list["capo_directory_service.types.ipv6_addr.Ipv6Addr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpv6Addrs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpv6Addrs:
    return list(data)
