"""Generated from Smithy shape ``com.amazonaws.storagegateway#IpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.ipv4_address

IpAddressList: TypeAlias = list["capo_storage_gateway.types.ipv4_address.IPV4Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpAddressList:
    return list(data)
