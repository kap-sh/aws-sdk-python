"""Generated from Smithy shape ``com.amazonaws.fsx#DnsIps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.ip_address

DnsIps: TypeAlias = list["aws_sdk_fsx.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIps) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIps:
    return list(data)
