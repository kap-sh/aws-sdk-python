"""Generated from Smithy shape ``com.amazonaws.directoryservice#DnsIpAddrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ip_addr

DnsIpAddrs: TypeAlias = list["capo_directory_service.types.ip_addr.IpAddr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpAddrs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpAddrs:
    return list(data)
