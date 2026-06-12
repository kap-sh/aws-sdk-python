"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareClientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.ipv4_or_ipv6_address_cidr

FileShareClientList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.ipv4_or_ipv6_address_cidr.Ipv4OrIpv6AddressCIDR"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileShareClientList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileShareClientList:
    return list(data)
