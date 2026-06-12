"""Generated from Smithy shape ``com.amazonaws.workspaces#DnsIpv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ipv6_address

DnsIpv6Addresses: TypeAlias = list["aws_sdk_workspaces.types.ipv6_address.Ipv6Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpv6Addresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpv6Addresses:
    return list(data)
