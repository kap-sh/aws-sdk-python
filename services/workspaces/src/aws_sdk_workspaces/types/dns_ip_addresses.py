"""Generated from Smithy shape ``com.amazonaws.workspaces#DnsIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_address

DnsIpAddresses: TypeAlias = list["aws_sdk_workspaces.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpAddresses:
    return list(data)
